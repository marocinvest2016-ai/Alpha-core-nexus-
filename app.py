import streamlit as st
import json
import os

st.set_page_config(page_title="وكالة تساوت الرقمية", page_icon="🏢", layout="wide")

st.sidebar.title("🏢 وكالة تساوت الرقمية")
st.sidebar.caption("قلعة السراغنة - في خدمتكم")
choice = st.sidebar.selectbox("اختر الخدمة", [
    "🏠 الرئيسية",
    "📋 عرض العقارات", 
    "💬 المحادثة الذكية مع وكيل تساوت",
    "📞 اتصل بنا"
])

def load_offers():
    if not os.path.exists("properties.json"): 
        return []
    with open("properties.json", "r", encoding="utf-8") as f: 
        return json.load(f)

YOUTUBE = "https://www.youtube.com/@studiotassaout"
FACEBOOK = "https://www.facebook.com/share/1DLCrNYLbV/"
MAPS = "https://share.google/M2eVdABaJqJEUqppj"
WHATSAPP = "https://wa.me/212691897126"
PHONE = "+212 691-897126"
EMAIL = "marocinvest201@gmail.com"

if choice == "🏠 الرئيسية":
    st.header("مرحباً بك في وكالة تساوت الرقمية 🏢")
    st.subheader("العقار والاعمال - قلعة السراغنة")
    st.write("بيع بقع سكنية وتجارية، اراضي فلاحية، فيرمات، كراء شقق ومكاتب")
    st.link_button("💬 واتساب مباشر", WHATSAPP, type="primary")

elif choice == "📋 عرض العقارات":
    st.header("📋 جميع العروض")
    offers = load_offers()
    if not offers:
        st.warning("لا توجد عروض حاليا")
    
    for offer in offers:
        with st.container(border=True):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(offer["image_url"], use_column_width=True)
            with col2:
                st.subheader(offer["title"])
                st.write(f"**النوع:** {offer['type']} | **المساحة:** {offer['surface']} m² | **الثمن:** {offer['price']:,} درهم")
                st.write(offer["description"])
                st.write(f"**المرجع:** `{offer['id']}`")
                
                wa_msg = f"https://wa.me/212{offer['contact_whatsapp'][1:]}?text=مهتم بـ {offer['title']} المرجع {offer['id']}"
                c1, c2 = st.columns(2)
                with c1:
                    st.link_button("📲 واتساب", wa_msg, type="primary")
                with c2:
                    st.link_button("📧 إيميل", f"mailto:{offer['contact_email']}")

elif choice == "💬 المحادثة الذكية مع وكيل تساوت":
    st.header("💬 المحادثة الذكية مع وكيل تساوت")
    user_input = st.text_input("اكتب سؤالك:", placeholder="مثال: بغيت بقعة تجارية 200 متر")
    if st.button("إرسال", type="primary"):
        offers = load_offers()
        results = [o for o in offers if user_input.lower() in o["title"].lower() or user_input.lower() in o["type"].lower() or user_input.lower() in o["description"].lower()]
        
        if results:
            st.success(f"✅ لقينا ليك {len(results)} عرض مناسب")
            for r in results:
                st.info(f"**{r['title']}**\n{r['surface']}m² - {r['price']:,} درهم")
        else:
            st.warning("ما لقيناش. ولكن عندنا عروض أخرى")
        
        st.write(f"📍 {MAPS}\n📞 {PHONE}\n💬 {WHATSAPP}\n▶️ {YOUTUBE}\n📘 {FACEBOOK}")
        st.link_button("💬 تواصل عبر واتساب", WHATSAPP, type="primary")

elif choice == "📞 اتصل بنا":
    st.header("📞 اتصل بنا")
    st.write(f"**الهاتف:** {PHONE}")
    st.write(f"**الإيميل:** {EMAIL}")
    st.write(f"**العنوان:** قلعة السراغنة")
    col1, col2 = st.columns(2)
    with col1: st.link_button("📍 الخريطة", MAPS)
    with col2: st.link_button("📲 واتساب", WHATSAPP)
