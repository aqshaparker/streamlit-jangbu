import streamlit as st
import pandas as pd
import numpy as np

# i. title
st.title("Dashboard Monitoring Performa")

# ii. header
st.header("Statistik Operasional")

# iii. subheader
st.subheader("Analisis Mingguan")

# vi. text untuk menulis paragraf
st.write("""
Laporan ini menyajikan data performa sistem berdasarkan input mingguan. 
Data di bawah ini mencakup perbandingan antara target produksi dan realisasi di lapangan.
""")

# iv. caption (bila di butuhkan)
st.caption("Raffa Aqsha Donesi 4232401033")

# v. code (untuk potongan code)
st.code("""
# Contoh cara memuat data
df = pd.read_csv('data_performa.csv')
st.line_chart(df)
""", language='python')

# vii. lalu data display
st.divider() # Garis pemisah untuk kerapihan

# Membuat data dummy untuk ditampilkan
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Produksi', 'Permintaan']
)

# a. tabel atau data frame
st.subheader("a. Tabel Data Frame")
st.dataframe(chart_data) 

# b. dan chart
st.subheader("b. Visualisasi Chart")
# Menggunakan st.line_chart (Chart bawaan Streamlit yang lebih interaktif)
st.line_chart(chart_data)