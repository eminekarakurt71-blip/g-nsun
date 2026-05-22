import subprocess
import streamlit as st

st.set_page_config(page_title="SVO English Backend", page_icon="🧠")
st.title("Görsel SVO İngilizce Sistemi - Backend")
st.write("✅ Flask sunucusu arka planda çalışıyor...")
st.info("API endpoints aktif. Uygulaman bu sunucu üzerinden çalışıyor.")

subprocess.Popen(["python", "app.py"])
