import streamlit as st
import os
import pandas as pd

st.set_page_config(page_title="وكالة السلام العقارية", page_icon="🏢", layout="wide")

# القائمة الجانبية
st.sidebar.title("🏢 وكالة السلام العقارية")
choice = st.sidebar.selectbox("اختر الخدمة", [
    "🏠 الرئيسية",
    "📋 عرض العقارات", 
    "💬 المحادثة الذكية مع وكيل تساوت",
    "📞 اتصل بنا"
])

def load_offers():
    file_path = "descriptions.txt"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines[1:] if "|" in line]

# الروابط الرسمية ديالك
YOUTUBE = "https://www.youtube.com/@studiotassaout"
FACEBOOK = "https://www.facebook.com/share/1DLCrNYLbV/"
MAPS = "https://share.google/M2eVdABaJqJEUqppj"
WHATSAPP = "https://wa.me/212691897126"
PHONE = "+212 691-897126"

if choice == "🏠 الرئيسية":
    st.header("مرحباً بك في وكالة السلام العقارية 🏢")
    st.subheader("قلعة السراغنة - خبرة
