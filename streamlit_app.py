import subprocess
import streamlit as st

st.title("Görsel SVO İngilizce Sistemi - Backend")
st.write("Flask sunucusu arka planda çalışıyor...")

subprocess.Popen(["python", "app.py"])
