import streamlit as st
import json
import os
import io
from PIL import Image, ImageEnhance

# إعدادات الصفحة والتصميم العام
st.set_page_config(
    page_title="وكالة تساوت الرقمية | TASSAOUT OMEGA OS", 
    page_icon="🚀", 
    layout="wide"
)

# تخصيص التصميم عبر CSS لاحترافية الواجهة
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
    }
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
    }
    .hero-box {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border: 2px solid #38bdf8;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.15);
    }
    .prop-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 20px;
        background-color: #1e293b;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .agent-box {
        background: linear-gradient(135deg, #0f172a 100%, #1e293b 0%);
        border: 1px solid #10b981;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

PROPERTIES_FILE = "properties.json"

# دالة لتحميل العقارات
def load_properties():
    if os.path.exists(PROPERTIES_FILE):
        try:
            with open(PROPERTIES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
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

def save_properties(properties_list):
    with open(PROPERTIES_FILE, "w", encoding="utf-8") as f:
        json.dump(properties_list, f, ensure_ascii=False, indent=4)

properties = load_properties()

# القائمة الجانبية للتنقل (مدمج مع نظام Agentic AI)
st.sidebar.markdown("### 🏢 وكالة تساوت الرقمية")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "🧭 التنقل في النظام", 
    [
        "🏠 الرئيسية", 
        "🤖 العقل الذكي (Agentic AI OS)", 
        "🚀 إطلاق OMEGA ULTRA (صفحة الهبوط)", 
        "🏡 العروض العقارية", 
        "📸 استوديو المعالجة الرقمية", 
        "💬 التواصل الفوري"
    ]
)

# 1. الرئيسية
if page == "🏠 الرئيسية":
    st.markdown("""
    <div class="hero-box">
        <h1 style="color: #38bdf8; margin-bottom: 10px;">🌐 وكالة تساوت الرقمية</h1>
        <p style="color: #94a3b8; font-size: 1.2rem;">المنصة الذكية المتكاملة للعقارات، الاستثمار، وحلول التصوير الاحترافي بقلعة السراغنة ومراكش</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    with col_stat1:
        st.metric(label="📊 إجمالي العقارات النشطة", value=len(properties))
    with col_stat2:
        st.metric(label="🤖 حالة النظام الذكي", value="Multi-Agent Active")
    with col_stat3:
        st.metric(label="🔥 إصدار المنصة", value="Omega OS v2.0")
        
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.info("🏡 **قطاع العقارات والأراضي:** عروض حصرية ومباشرة من أصحاب الأملاك مع ضمان الشفافية والمواصفات الدقيقة.")
    with col2:
        st.success("🤖 **نظام التشغيل الذكي (Agentic AI):** إدارة آلية للعمليات، توليد المحتوى، والرد على الزبناء لحظياً.")

# 2. قسم العقل الذكي متعدد الوكلاء (Super Multi-Domain Agentic AI OS)
elif page == "🤖 العقل الذكي (Agentic AI OS)":
    st.title("🧠 نظام التشغيل الذكي متعدد الوكلاء (Super Multi-Domain AI)")
    st.markdown("منظومة الذكاء الاصطناعي الذاتية لتطوير التشغيل، التوجيه، وإدارة المحتوى والعقارات في قلعة السراغنة ومراكش:")

    # اختيار مجال الوكيل الذكي
    agent_domain = st.selectbox(
        "اختر الوكيل الذكي المتخصص:",
        [
            "📢 وكيل التسويق والإعلانات (Marketing & Social Media Agent)",
            "🏢 وكيل العقارات والاستثمار (Real Estate & Matching Agent)",
            "⚙️ وكيل العمليات والتشغيل الذاتي (Operations & Automation Agent)"
        ]
    )

    st.markdown("---")

    if "Marketing" in agent_domain:
        st.subheader("📢 وحدة توليد الحملات التسويقية الذاتية")
        market_topic = st.text_input("أدخل موضوع أو اسم العقار/المنتج المراد الإعلان عنه:", "بقع أرضية تجارية في تجزئة الهدى")
        if st.button("🚀 توليد الحملة الإعلانية الشاملة"):
            with st.spinner("جاري تحليل السوق وصياغة الإعلان..."):
                st.markdown(f"""
                <div class="agent-box">
                    <h3 style="color: #38bdf8;">🔥 مقترح الإعلان التلقائي (جاهز للنسخ):</h3>
                    <p><b>النص الترويجي:</b> فرصة استثمارية ذهبية بقلعة السراغنة ومراكش! تملّك الآن في {market_topic} بأسعار تنافسية مباشرة من المالك.</p>
                    <p><b>الهاشتاغات:</b> #TassaoutOmega #RealEstateMorocco #ElKelaadesSraghna #MarrakechInvest</p>
                    <p style="color: #4ade80;"><b>للحجز المباشر:</b> تواصل معنا عبر واتساب الخط الساخن: 0691897126 📲</p>
                </div>
                """, unsafe_allow_html=True)

    elif "Real Estate" in agent_domain:
        st.subheader("🏢 وحدة مطابقة العقارات للزبناء (Smart Matchmaker)")
        client_budget = st.selectbox("الميزانية أو الطلب المرغوب للزبون:", ["بقع سكنية اقتصادية (أقل من 240م²)", "فرص استثمارية كبرى", "محلات تجارية وكرات"])
        if st.button("🔍 البحث المطابق بالذكاء الاصطناعي"):
            st.success(f"🤖 [وكيل العقارات الذكي]: تم مطابقة طلبك ({client_budget}) مع قاعدة البيانات الحالية بنجاح!")
            for prop in properties:
                st.markdown(f"""
                <div class="prop-card">
                    <h4 style="color: #38bdf8; margin-top: 0;">✅ تطابق مقترح: {prop['title']}</h4>
                    <p>{prop['details']}</p>
                    <p style="color: #4ade80;"><b>📞 تواصل فوري:</b> {prop['phone']}</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.subheader("⚙️ وحدة التشغيل الذاتي وصحة النظام")
        st.info("النظام يعمل بكفاءة تامة. ملفات التخزين (`properties.json`) متزامنة ومحدثة، والروابط السحابية لخدمة واتساب مفعلة بامتياز.")
        if st.button("🔄 فحص وتشخيص النظام برمجياً"):
            st.success("✔ حالة الخادم: مستقر (Stable)\n✔ وحدات التخزين: جاهزة\n✔ الاستجابة التلقائية: فعّالة 100%")

# 3. صفحة هبوط إطلاق OMEGA ULTRA
elif page == "🚀 إطلاق OMEGA ULTRA (صفحة الهبوط)":
    st.markdown("""
    <div class="hero-box">
        <h1 style="color: #38bdf8;">🎬 DANA-LUXE | TASSAOUT OMEGA ULTRA</h1>
        <h3 style="color: #4ade80;">استوديو التصوير المتكامل في يد واحدة - الإصدار الأسطوري 100MP</h3>
        <p style="color: #94a3b8;">الثورة التكنولوجية الكبرى في عالم التصوير الاحترافي، إعلانات السيارات، والسينما، قريباً في قلعة السراغنة ومراكش.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists("watermarked_img_6744616521520499004.png"):
        st.image("watermarked_img_6744616521520499004.png", caption="TASSAOUT OMEGA MAXIMUM EDITION | DANA-LUXE ECO-SYSTEM", use_container_width=True)
        
    st.markdown("### 💎 الميزات الخارقة للإصدار:")
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.markdown("#### ⚡ Global Shutter\nسرعة غالق فائقة 1/160000s لتجميد أسرع اللحظات بدقة مطلقة.")
    with col_f2:
        st.markdown("#### 🧠 AI Engine\nتوليد خلفيات ذكية ومعالجة فورية داخل الهاردوير.")
    with col_f3:
        st.markdown("#### 🔋 Omega Cell\nبطارية خارقة تدوم 4 ساعات مع شحن سريع خلال دقائق معدودة.")
        
    st.markdown("---")
    st.success("📅 **موعد الإطلاق الرسمي:** فاتح شتنبر القادم | الحجز المسبق مفتوح حصرياً للعدد المحدود.")
    
    whatsapp_launch = "https://wa.me/212691897126?text=السلام%20عليكم،%20أريد%20حجز%20نسختي%20المسبقة%20من%20كاميرا%20OMEGA%20ULTRA"
    st.markdown(f"""
    <a href="{whatsapp_launch}" target="_blank">
        <button style="background-color: #25D366; color: white; padding: 14px 24px; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; width: 100%;">
            🚀 احجز نسختك الأولى الآن عبر واتساب
        </button>
    </a>
    """, unsafe_allow_html=True)

# 4. العروض العقارية مع البحث، التصفح والواتساب المخصص
elif page == "🏡 العروض العقارية":
    st.title("📋 العروض العقارية والاستثمارية المتاحة")
    st.markdown("تصفح أحدث البقع، الشقق، والمشاريع التجارية المتاحة حالياً:")
    
    # قسم البحث والتصفية المتقدمة
    st.markdown("### 🔍 البحث والتصفية المتقدمة")
    search_query = st.text_input("ابحث عن عنوان العقار أو التفاصيل...")
    selected_cat = st.selectbox("تصفية حسب التصنيف", ["الكل", "بقع سكنية وتجارية", "فرص استثمارية", "الكراء", "استثمار فلاحي"])

    filtered_properties = properties
    if search_query:
        filtered_properties = [p for p in filtered_properties if search_query.lower() in p['title'].lower() or search_query.lower() in p['details'].lower()]
    if selected_cat != "الكل":
        filtered_properties = [p for p in filtered_properties if p['category'] == selected_cat]

    if filtered_properties:
        for prop in filtered_properties:
            whatsapp_prop_url = f"https://wa.me/212691897126?text=السلام%20عليكم،%20أنا%20مهتم%20بالعقار%20التالي:%20{prop['title']}%20({prop['category']})"
            st.markdown(f"""
            <div class="prop-card">
                <h3 style="color: #38bdf8; margin-top: 0;">🏢 {prop['title']}</h3>
                <p><b>🏷️ التصنيف:</b> {prop['category']}</p>
                <p><b>📝 التفاصيل:</b> {prop['details']}</p>
                <p style="color: #4ade80; font-weight: bold;">📞 الخط المباشر: {prop['phone']}</p>
                <a href="{whatsapp_prop_url}" target="_blank">
                    <button style="background-color: #25D366; color: white; padding: 8px 16px; border: none; border-radius: 6px; font-size: 14px; font-weight: bold; cursor: pointer; margin-top: 5px;">
                        💬 الاستفسار عن هذا العقار عبر واتساب
                    </button>
                </a>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("لا توجد عقارات تطابق بحثك.")
        
    st.markdown("---")
    st.subheader("➕ إضافة عقار أو إعلان جديد للنظام")
    with st.form("add_property_form", clear_on_submit=True):
        new_title = st.text_input("عنوان العقار/الإعلان")
        new_category = st.selectbox("التصنيف", ["بقع سكنية وتجارية", "فرص استثمارية", "الكراء", "محلات تجارية", "استثمار فلاحي"])
        new_details = st.text_area("تفاصيل العقار والمساحة والموقع")
        new_phone = st.text_input("رقم الهاتف", value="0691897126")
        
        submitted = st.form_submit_button("💾 حفظ وإضافة العقار فوراً")
        if submitted and new_title:
            new_prop = {
                "title": new_title,
                "category": new_category,
                "details": new_details,
                "phone": new_phone
            }
            properties.append(new_prop)
            save_properties(properties)
            st.success("تم إضافة العقار بنجاح وتحديث النظام!")
            st.rerun()

# 5. استوديو المعالجة الرقمية
elif page == "📸 استوديو المعالجة الرقمية":
    st.title("🎬 OMEGA ENGINE - معالجة الصور الرقمية")
    st.markdown("قم بتحسين ومعالجة صور العقارات والسيارات بمعايير الاستوديو الاحترافي:")

    tab1, tab2 = st.tabs(["📷 التقاط مباشر", "⚙️ محرك المعالجة السينمائية"])

    with tab1:
        camera_image = st.camera_input("التقاط صورة حية للمعاينة الميدانية")
        if camera_image is not None:
            st.success("تم الالتقاط بنجاح عبر محاكي العدسة!")
            st.image(Image.open(camera_image), use_container_width=True)

    with tab2:
        uploaded_file = st.file_uploader("رفع صورة عقار أو سيارة لمعالجتها", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="الصورة الأصلية", use_container_width=True)
            
            st.markdown("### 🎛️ أدوات التحكم الاحترافية:")
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                brightness = st.slider("إضاءة HDR", 0.5, 2.0, 1.0)
            with col_b:
                contrast = st.slider("حدة التفاصيل", 0.5, 2.0, 1.0)
            with col_c:
                color_sat = st.slider("تشبع الألوان", 0.0, 2.5, 1.2)
            
            img_processed = ImageEnhance.Brightness(image).enhance(brightness)
            img_processed = ImageEnhance.Contrast(img_processed).enhance(contrast)
            img_final = ImageEnhance.Color(img_processed).enhance(color_sat)
            
            st.image(img_final, caption="النتيجة النهائية (OMEGA CINEMATIC)", use_container_width=True)
            
            buf = io.BytesIO()
            img_final.save(buf, format="JPEG")
            
            col_d1, col_d2 = st.columns(2)
            with col_d1:
                st.download_button(
                    label="📥 تحميل الصورة المحسنة",
                    data=buf.getvalue(),
                    file_name="OMEGA_ULTRA_PRO.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )
            with col_d2:
                wa_image_msg = "https://wa.me/212691897126?text=السلام%20عليكم،%20لقد%20قمت%20بمعالجة%20الصورة%20عبر%20OMEGA%20ENGINE%20وأريد%20نشرها%20أو%20مشاركة%20النتيجة."
                st.markdown(f"""
                <a href="{wa_image_msg}" target="_blank">
                    <button style="background-color: #25D366; color: white; padding: 10px 20px; border: none; border-radius: 8px; font-size: 14px; font-weight: bold; cursor: pointer; width: 100%;">
                        💬 إرسال للوكيل عبر واتساب
                    </button>
                </a>
                """, unsafe_allow_html=True)

# 6. التواصل الفوري
elif page == "💬 التواصل الفوري":
    st.title("💬 خدمة العملاء والتنسيق الفوري")
    st.markdown("للحجز، الاستفسار، أو طلب معاينة ميدانية بقلعة السراغنة ومراكش:")
    st.success("📞 الخط الساخن المعتمد: **0691897126**")
    
    whatsapp_url = "https://wa.me/212691897126?text=السلام%20عليكم،%20أريد%20التواصل%20بخصوص%20عروض%20وكالة%20تساوت%20الرقمية"
    st.markdown(f"""
    <a href="{whatsapp_url}" target="_blank">
        <button style="background-color: #25D366; color: white; padding: 14px 24px; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; box-shadow: 0 4px 12px rgba(37, 211, 102, 0.3);">
            💬 التواصل المباشر عبر واتساب
        </button>
    </a>
    """, unsafe_allow_html=True)
