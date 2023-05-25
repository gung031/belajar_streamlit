import streamlit as st

st.set_page_config(
    page_title="Mari belajar streamlit",
    layout="wide"
)

# Menulis teks di streamlit

st.write("Hello World!")

#WIDGET <- input element
ini_tombol = st.button("Ini tombol")
ini_tombol

saya_setuju = st.checkbox("Centang jika setuju")
if saya_setuju:
    st.write("anda setuju untuk belajar lebih giat")
else:
    st.write("Lebih giat")

kalender = st.date_input(
    "masukkan tanggal"
)

kalender

# Container and layouting
