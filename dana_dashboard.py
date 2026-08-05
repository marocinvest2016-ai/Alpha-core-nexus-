import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="Alpha Core Nexus", layout="wide")

# --- إنشاء مجلدات وملفات لو مش موجودة ---
os.makedirs("uploads", exist_ok=True)
PROPERTIES_FILE = "properties.json"
CARS_FILE = "cars.json"

def load_data(file):
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_data(data, file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# --- واجهة Alpha Core Nexus ---
st.title("🧠 Alpha Core Nexus v20.3")
st.caption("Super Multi-Domain Agentic AI System | Maroc Invest 2016")

tab1, tab2, tab3 = st.tabs(["🏠 العقارات", "🚗 السيارات", "🤖 الوكلاء"])

# --- TAB 1: العقارات ---
with tab1:
    st.header("إدارة العقارات - @ameurimmobilier Agent")
    properties = load_data(PROPERTIES_FILE)
    
    with st.form("add
