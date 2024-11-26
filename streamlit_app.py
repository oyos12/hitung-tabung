import streamlit as st
import math, time

st.title("Menghitung :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukkan Jari-Jari (cm): ",0)
t = st.number_input("Masukkan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  loading = st.progress(0)
  for i in range(100):
    time.sleep(0.01)
    loading.progress(i+1)
