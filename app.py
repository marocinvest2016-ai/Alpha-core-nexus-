import streamlit as st
import json
import os

st.set_page_config(page_title="وكالة تساوت الرقمية للعقار والأعمال", page_icon="🏢", layout="wide")

st.sidebar.title("🏢 وكالة تساوت الرقمية")
page = st.sidebar.selectbox("اختر القسم", ["🏠 الرئيسية", "🏡 عرض العقارات", "💬 التواصل المباشر"])

# دالة لتحميل العقارات من الملف الخارجي
def load_properties():
    if os.path.exists("properties.json"):
        with open("properties.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return []

if page == "🏠 الرئيسية":
    st.title("🌐 وكالة تساوت الرقمية - قلعة السراغنة ومراكش")
    st.subheader("منظومة إدارة العقارات والاستثمار الفلاحي")
    st.markdown("مرحباً بك في المنصة الذكية لإدارة العروض العقارية والتجارية.")
    st.info("💡 استخدم القائمة الجانبية لتصفح العقارات المتاحة.")

elif page == "🏡 عرض العقارات":
    st.title("📋 العروض العقارية والاستثمارية المتاحة")
    
    properties = load_properties()
    
    if properties:
        for prop in properties:
            st.markdown(f"""
            <div style="padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 15px; background-color: #f9f9f9;">
                <h3 style="color: #2c3e50; margin-bottom: 5px;">🏢 {prop['title']}</h3>
                <p><b>التصنيف:</b> {prop['category']}</p>
                <p><b>التفاصيل:</b> {prop['details']}</p>
                <p style="color: #27ae60; font-weight: bold;">📞 للتواصل المباشر: {prop['phone']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("لا توجد عقارات مضافة حالياً.")

elif page == "💬 التواصل المباشر":
    st.title("💬 خدمة العملاء والتنسيق الفوري")
    st.markdown("للحجز، الاستفسار، أو تنسيق المعاينات الميدانية بقلعة السراغنة ومراكش:")
    st.success("📞 خط الاتصال المباشر: **0691897126**")
