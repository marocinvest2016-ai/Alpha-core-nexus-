import streamlit as st
import json
import os
from PIL import Image, ImageEnhance

# إعدادات الصفحة
st.set_page_config(
    page_title="وكالة تساوت الرقمية للعقار والتكنولوجيا", 
    page_icon="📸", 
    layout="wide"
)

# القائمة الجانبية
st.sidebar.title("🏢 وكالة تساوت الرقمية")
page = st.sidebar.selectbox(
    "اختر القسم", 
    [
        "🏠 الرئيسية", 
        "🏡 العروض العقارية", 
        "📸 استوديو الكاميرا والتصوير التفاعلي", 
        "💬 التواصل المباشر"
    ]
)

# دالة لتحميل العقارات من الملف الخارجي
def load_properties():
    if os.path.exists("properties.json"):
        with open("properties.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return [
        {
            "title": "بقع سكنية وتجارية في تجزئة الهدى", 
            "category": "بقع سكنية وتجارية", 
            "details": "من 80م² إلى 240م² مع موقع استراتيجي وأسعار تنافسية", 
            "phone": "0691897126"
        },
        {
            "title": "بقع لبناء عمارات أو مشاريع تجارية", 
            "category": "فرص استثمارية", 
            "details": "مساحات من 80م² إلى 240م² عند أصحاب الأملاك مباشرة", 
            "phone": "0691897126"
        }
    ]

# 1. صفحة الرئيسية
if page == "🏠 الرئيسية":
    st.title("🌐 وكالة تساوت الرقمية - قلعة السراغنة ومراكش")
    st.subheader("منظومة إدارة العقارات والاستثمار والتصوير الرقمي الذكي")
    st.markdown("مرحباً بك في المنصة الذكية المتكاملة للعروض العقارية وحلول الكاميرات الاحترافية.")
    st.info("💡 استخدم القائمة الجانبية لتصفح الأقسام وتجربة الاستوديو الرقمي.")

# 2. صفحة العروض العقارية
elif page == "🏡 العروض العقارية":
    st.title("📋 العروض العقارية والاستثمارية المتاحة")
    
    properties = load_properties()
    
    if properties:
        for prop in properties:
            st.markdown(f"""
            <div style="padding: 15px; border-radius: 10px; border: 1px solid #334155; margin-bottom: 15px; background-color: #1e293b; color: #f8fafc;">
                <h3 style="color: #38bdf8; margin-bottom: 5px;">🏢 {prop['title']}</h3>
                <p><b>التصنيف:</b> {prop['category']}</p>
                <p><b>التفاصيل:</b> {prop['details']}</p>
                <p style="color: #4ade80; font-weight: bold;">📞 للتواصل المباشر: {prop['phone']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("لا توجد عقارات مضافة حالياً.")

# 3. صفحة استوديو الكاميرا والتصوير التفاعلي (الميزة الجديدة)
elif page == "📸 استوديو الكاميرا والتصوير التفاعلي":
    st.title("🎬 DANA-LUXE | TASSAOUT OMEGA ULTRA - استوديو المعاينة")
    st.markdown("قم بتوثيق أو معاينة العقارات والسيارات والمنتجات مباشرة من خلال محاكي الكاميرا الذكي:")

    tab1, tab2 = st.tabs(["📷 التقاط صورة مباشرة", "📤 رفع ومعالجة صورة عقار/منتج"])

    with tab1:
        st.subheader("التقاط صورة ميدانية")
        camera_image = st.camera_input("وجه الكاميرا لالتقاط صورة فورية للمعاينة")
        if camera_image is not None:
            st.success("تم التقاط الصورة بنجاح بواسطة عدسة OMEGA!")
            img = Image.open(camera_image)
            st.image(img, caption="الصورة الملتقطة للمعاينة الميدانية", use_container_width=True)

    with tab2:
        st.subheader("معالجة وتحسين صور العقارات والسيارات")
        uploaded_file = st.file_uploader("اختر صورة من جهازك (عقار، سيارة، منتج)", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="الصورة الأصلية", use_container_width=True)
            
            # خيارات المعالجة الرقمية محاكاة لوضع OMEGA
            st.markdown("### ⚙️ أدوات المعالجة والتحسين (Quantum Engine):")
            brightness = st.slider("تحسين الإضاءة والنطاق الديناميكي (HDR)", 0.5, 2.0, 1.0)
            contrast = st.slider("تحسين التفاصيل والتباين (100MP Mode)", 0.5, 2.0, 1.0)
            
            # تطبيق التعديلات
            enhancer_b = ImageEnhance.Brightness(image)
            img_processed = enhancer_b.enhance(brightness)
            enhancer_c = ImageEnhance.Contrast(img_processed)
            img_final = enhancer_c.enhance(contrast)
            
            st.image(img_final, caption="الصورة بعد المعالجة الاحترافية", use_container_width=True)
            st.success("جاهزة للنشر في منصات العرض والإعلانات الفورية بقلعة السراغنة ومراكش!")

    st.success("📞 للتواصل المباشر وطلب الحجز: **0691897126**")

# 4. صفحة التواصل المباشر
elif page == "💬 التواصل المباشر":
    st.title("💬 خدمة العملاء والتنسيق الفوري")
    st.markdown("للحجز، الاستفسار، أو تنسيق المعاينات الميدانية بقلعة السراغنة ومراكش:")
    st.success("📞 خط الاتصال المباشر: **0691897126**")
