import streamlit as st
import json
import os

# إعدادات الصفحة
st.set_page_config(
    page_title="وكالة تساوت الرقمية للعقار والتكنولوجيا", 
    page_icon="🏢", 
    layout="wide"
)

# القائمة الجانبية
st.sidebar.title("🏢 وكالة تساوت الرقمية")
page = st.sidebar.selectbox(
    "اختر القسم", 
    [
        "🏠 الرئيسية", 
        "🏡 العروض العقارية", 
        "📸 استوديو DANA-LUXE OMEGA", 
        "💬 التواصل المباشر"
    ]
)

# دالة لتحميل العقارات من الملف الخارجي
def load_properties():
    if os.path.exists("properties.json"):
        with open("properties.json", "r", encoding="utf-8") as f:
            return json.load(f)
    # القائمة الافتراضية في حال عدم وجود الملف الخارجي بعد
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
        },
        {
            "title": "شقق ومكاتب للكراء المهني والسكني", 
            "category": "الكراء", 
            "details": "مواقع استراتيجية وجاهزة للاستغلال الفوري بقلعة السراغنة", 
            "phone": "0691897126"
        }
    ]

# 1. صفحة الرئيسية
if page == "🏠 الرئيسية":
    st.title("🌐 وكالة تساوت الرقمية - قلعة السراغنة ومراكش")
    st.subheader("منظومة إدارة العقارات والاستثمار الفلاحي والتكنولوجي")
    st.markdown("مرحباً بك في المنصة الذكية المتكاملة للعروض العقارية والتجارية وحلول الاستوديو الرقمي.")
    st.info("💡 استخدم القائمة الجانبية لتصفح الأقسام والعروض المتاحة.")

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

# 3. صفحة استوديو الكاميرا الاحترافية
elif page == "📸 استوديو DANA-LUXE OMEGA":
    st.title("🎬 DANA-LUXE | TASSAOUT OMEGA ULTRA")
    st.markdown("### استوديو التصوير المتكامل في يد واحدة (إصدار أوميغا الأقصى)")
    
    st.markdown("""
    <div style="padding: 15px; border-radius: 10px; border: 1px solid #38bdf8; background-color: #0f172a; color: #e2e8f0; margin-bottom: 20px;">
        <h4 style="color: #38bdf8; margin-top: 0;">⚙️ المواصفات الثورية المختصرة:</h4>
        <ul>
            <li><b>الحساس:</b> OMEGA-SENSOR 100MP BSI Stacked MF + Quantum ISO 50 - 2,048,000</li>
            <li><b>المعالج:</b> TRIPLE OMEGA ENGINE (8K + AI + RAW في نفس الوقت)</li>
            <li><b>الغالق:</b> GLOBAL SHUTTER TITANIUM 1/160000s</li>
            <li><b>أوضاع الفيرموير:</b> 15 وضعاً متقدماً (توليد خلفيات AI، مسح 3D للأوتوموبيل، تتبع النجوم Astro، و 32-bit Float HDR).</li>
        </ul>
        <p style="color: #4ade80; font-weight: bold; margin-bottom: 0;">📅 موعد الإطلاق الرسمي: فاتح شتنبر القادم بقلعة السراغنة ومراكش.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("📞 للحجز المسبق والتواصل السريع: **0691897126**")

# 4. صفحة التواصل المباشر
elif page == "💬 التواصل المباشر":
    st.title("💬 خدمة العملاء والتنسيق الفوري")
    st.markdown("للحجز، الاستفسار، أو تنسيق المعاينات الميدانية بقلعة السراغنة ومراكش:")
    st.success("📞 خط الاتصال المباشر: **0691897126**")
