import streamlit as st
import os

st.set_page_config(page_title="وكالة السلام العقارية", page_icon="🏢", layout="wide")

st.sidebar.title("🏢 وكالة السلام العقارية")
choice = st.sidebar.selectbox("اختر الخدمة", [
    "🏠 الرئيسية",
    "📋 عرض العقارات", 
    "💬 المحادثة الذكية مع وكيل تساوت",
    "📞 اتصل بنا"
])

def load_offers():
    if not os.path.exists("descriptions.txt"): 
        return []
    with open("descriptions.txt", "r", encoding="utf-8") as f: 
        return [line.strip() for line in f.readlines()[1:] if "|" in line]

YOUTUBE = "https://www.youtube.com/@studiotassaout"
FACEBOOK = "https://www.facebook.com/share/1DLCrNYLbV/"
MAPS = "https://share.google/M2eVdABaJqJEUqppj"
WHATSAPP = "https://wa.me/212691897126"
PHONE = "+212 691-897126"

if choice == "🏠 الرئيسية":
    st.header("مرحباً بك في وكالة السلام العقارية 🏢")
    st.subheader("قلعة السراغنة")
    st.link_button("💬 واتساب مباشر", WHATSAPP, type="primary")

elif choice == "📋 عرض العقارات":
    st.header("📋 جميع العروض")
    for offer in load_offers(): 
        st.info(offer)

elif choice == "💬 المحادثة الذكية مع وكيل تساوت":
    st.header("💬 المحادثة الذكية مع وكيل تساوت")
    user_input = st.text_input("اكتب سؤالك:", placeholder="مثال: بغيت بقعة تجارية")
    if st.button("إرسال", type="primary"):
        offers = load_offers()
        found = any(user_input.lower() in o.lower() for o in offers)
        if found:
            st.success(f"مرحباً بك في وكالة السلام 🏢\n\n✅ لقينا ليك عرض\n📍 {MAPS}\n📞 {PHONE}\n💬 {WHATSAPP}\n▶️ {YOUTUBE}\n📘 {FACEBOOK}")
            st.link_button("💬 تواصل عبر واتساب", WHATSAPP, type="primary")
        else:
            st.warning(f"ما لقيناش. تواصل: {PHONE}\n💬 {WHATSAPP}")

elif choice == "📞 اتصل بنا":
    st.header("📞 اتصل بنا")
    st.write(f"الهاتف: {PHONE}")
    st.link_button("📍 الخريطة", MAPS)
