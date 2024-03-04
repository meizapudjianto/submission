import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load cleaned data
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# membaca model
bike = pickle.load(open('dashboard/bike.sav', 'rb'))

with st.sidebar:
    # Menambahkan logo perusahaan di sidebar
    st.image("logo.png")
    
    # Mengambil start_date & end_date dari date_input
    min_date = pd.to_datetime(day_df['dteday']).min()
    max_date = pd.to_datetime(day_df['dteday']).max()
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Menyiapkan berbagai dataframe
bike_df = hour_df.merge(day_df, on='dteday', how='inner', suffixes=('_hour', '_day'))

# judul web
st.header('Bike Sharing :sparkles:')

# jumlah jam penyewaan sepeda pada setiap bulannya
st.subheader("Jumlah jam penyewaan sepeda setiap bulan")

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(data=day_df, x='mnth', y='cnt', ax=ax, color='#1f77b4')
ax.set(title='Jumlah Jam Penyewaan Sepeda Setiap Bulan')

st.pyplot(fig)

# rata-rata penyewaan per jam
st.subheader("Rata-rata penyewaan per jam")
sewa_jam = bike_df.groupby('hr')['cnt_hour'].mean()

fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x=sewa_jam.index, y=sewa_jam.values, color='#1f77b4')
ax.set(title='Rata - Rata Penyewaan per Jam', xlabel='Jam', ylabel='Rata - Rata')

st.pyplot(fig)
