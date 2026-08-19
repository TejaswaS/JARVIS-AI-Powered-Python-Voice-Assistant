import streamlit as st
from memory import Memory

mem = Memory()
st.title("JARVIS Dashboard")

history = mem.load()

for item in history:
    st.write("You:", item["user"])
    st.write("JARVIS:", item["jarvis"])

#http://localhost:8501    
#python -m streamlit run dashboard.py
