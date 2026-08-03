import streamlit as st
import pandas as pd
import os

# --- دالة قراءة العروض من descriptions.txt ---
def load_offers():
    file_path = "descriptions.txt"
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # أول سطر هو اسم الوكالة، الباقي عروض
    offers = [line.strip() for line in lines[1:] if "|" in line]
    return offers

# --- قسم المحادثة الذكية ---
st.header("💬 المحادثة الذكية مع وكيل تساوت")
st.write("اسأل عن عقارات قلعة السراغنة...")

user_input = st.text_input("اكتب سؤالك هنا:", key="chat_input")

if st.button("إرسال", key="send_chat"):
    if user_input:
        offers = load_offers()
        
        # الجواب النهائي المباشر
        response = f"""مرحباً بك في وكالة تساوت الرقمية للعقار والأعمال 🏢

طلبك: {user_input}

للاستفسار والحجز والمعاينة تواصل معنا مباشرة:
📞 0691897126

قلعة السراغنة - فريقنا جاهز 24/7"""
        
        st.success(response)
    else:
        st.warning("من فضلك اكتب سؤالك")
