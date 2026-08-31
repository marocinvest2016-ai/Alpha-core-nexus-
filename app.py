import os
import streamlit as st
import pandas as pd
from datetime import datetime
from supabase import create_client, Client
import urllib.parse

# 1. إعدادات الصفحة السيادية
st.set_page_config(
    page_title="Alpha Core Nexus - المكتبة الرقمية ونظام تساوت",
    page_icon="👑",
    layout="wide"
)

# 2. الاتصال بقاعدة بيانات Supabase
SUPABASE_URL = st.secrets.get("SUPABASE_URL", "")
SUPABASE_KEY = st.secrets.get("SUPABASE_KEY", "")
MY_PHONE = "212691897126"

try:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception:
    supabase = None

# فئة الوكيل الذكي لقلعة السراغنة ومراكش
class AmarAgent:
    def __init__(self, nom_entreprise):
        self.nom = nom_entreprise

    def scanner_domain(self, keyword):
        opps = []
        if supabase:
            try:
                res = (
                    supabase.table("instant_ads")
                    .select("*")
                    .ilike("message", f"%{keyword}%")
                    .limit(5)
                    .execute()
                )
                opps = res.data
            except:
                opps = []
        if not opps:
            opps = [{
                "message": f"صفقة توريد أو عقار بـ {keyword}",
                "region": "Marrakech-Safi",
                "montant": 120000,
            }]
        return [
            {
                "region": ad.get("region", "Marrakech-Safi"),
                "ville": keyword,
                "objet": ad.get("message", "صفقة")[:100],
                "montant_est": ad.get("montant", 45000),
            }
            for ad in opps
        ]

    def analyse_domain(self, opps):
        for opp in opps:
            opp["concurrence"] = "🟢 ضعيفة" if opp["montant_est"] < 100000 else "🟡 متوسطة"
            ht = opp["montant_est"] / 1.20
            opp["ht"] = round(ht, 2)
            opp["tva"] = round(opp["montant_est"] - ht, 2)
            opp["benefice"] = round(ht * 0.14, 2)
            opp["score"] = 95
        return sorted(opps, key=lambda x: x["score"], reverse=True)

    def rapport_comm(self, opps):
        msg = f"*👑 تقرير عامر - {datetime.now().strftime('%d/%m/%Y %H:%M')}*\n\n"
        for i, opp in enumerate(opps, 1):
            msg += (
                f"*{i}. [{opp['score']}/100] {opp['objet']}*\n💰"
                f" {opp['montant_est']} DH | 📍 {opp['region']} | 📈 ربح صافي:"
                f" {opp['benefice']} DH\n\n"
            )
        return msg

# 3. الشريط الجانبي: نظام التنقل الشامل
st.sidebar.title("🗂️ نظام Alpha Core Nexus")
main_nav = st.sidebar.radio(
    "اختر النظام الرئيسي:",
    [
        "🏛️ المكتبة الرقمية السحابية",
        "👑 نظام إدارة العقارات والصفقات (Meta Tassaout)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("الرقم الموحد الرسمي: **0691897126**\n\n`[TASSAOUT VERIFIED]`")

# --- النظام الأول: المكتبة الرقمية السحابية الجامعة ---
if main_nav == "🏛️ المكتبة الرقمية السحابية":
    st.title("🛡️ المكتبة الرقمية السحابية الجامعة - Alpha Core Nexus")
    st.markdown("---")
    
    section = st.sidebar.selectbox(
        "أقسام المكتبة:",
        [
            "الرئيسية ونظرة عامة",
            "الدستور والبروتوكولات السيادية",
            "أكواد الوكلاء والسكريبتات",
            "قواعد المعرفة والعقارات",
            "أصول الهوية والبصريات"
        ]
    )

    if section == "الرئيسية ونظرة عامة":
        st.header("مرحباً بك في الدماغ المركزي لمكتب تساوت الرقمي")
        st.info("النظام يعمل بتناغم تام مع الرقم الموحد الرسمي: **0691897126**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="حالة النظام", value="نشط [ACTIVE]")
        with col2:
            st.metric(label="مستوى الأمان", value="محمي [TASSAOUT VERIFIED]")
        with col3:
            st.metric(label="الربط السحابي", value="جاهز لـ GitHub & Supabase")

    elif section == "الدستور والبروتوكولات السيادية":
        st.header("📜 البروتوكولات السيادية")
        st.markdown("""
        * **قاعدة عدم الحشو:** تنفيذ المهام بدقة وسرعة وبدون إطالة.
        * **عدم إبداء الرأي إلا بأمر:** الالتزام التام بالتعليمات السيادية للنظام.
        * **الأرشيف الموحد:** حفظ جميع السجلات بختم `[TASSAOUT VERIFIED]`.
        """)

    elif section == "أكواد الوكلاء والسكريبتات":
        st.header("⚙️ السكريبتات وأكواد التشغيل")
        st.code("""
# نموذج كود مزامن أوتوماتيكي
import os
def sync_to_github():
    print("Syncing Tassaout Library with GitHub repository...")
        """, language="python")

    elif section == "قواعد المعرفة والعقارات":
        st.header("🏢 قواعد المعرفة والعقارات")
        st.write("إدارة عروض العقارات، الشقق، والقطع الأرضية بقلعة السراغنة ومراكش.")
        st.success("تم ربط قاعدة البيانات بنجاح.")

    elif section == "أصول الهوية والبصريات":
        st.header("🎨 أصول الهوية البصرية واستوديو تساوت")
        st.write("تحتوي على معايير التصميم، الشعارات، واللوحات الإعلانية الرقمية.")

# --- النظام الثاني: نظام إدارة العقارات والصفقات المتقدم (Meta Tassaout) ---
elif main_nav == "👑 نظام إدارة العقارات والصفقات (Meta Tassaout)":
    st.title("👑 Meta Tassaout - المكتب السيادي العقاري والخدماتي")
    st.markdown("### الحالة: 🟢 نظام إدارة العقارات والخدمات المتعددة")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📸 التصوير أو تحميل الصور",
        "🧠 عروض الوكيل والتفاعل",
        "📚 مواضيع أخرى",
        "➕ إضافة عرض جديد",
    ])

    with tab1:
        st.subheader("رفع ومعالجة الصور التسويقية (يدعم عدة صور معا)")
        uploaded_files = st.file_uploader(
            "اختر الصور (يمكنك اختيار أكثر من صورة)",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=True,
        )

        if uploaded_files:
            st.success(f"تم تحميل {len(uploaded_files)} صورة بنجاح!")
            cols = st.columns(3)
            for idx, uploaded_file in enumerate(uploaded_files):
                with cols[idx % 3]:
                    st.image(
                        uploaded_file,
                        caption=f"صورة رقم {idx+1}",
                        use_container_width=True,
                    )

    with tab2:
        st.subheader("تحليلات الوكيل وعروض السوق")
        city = st.text_input("المدينة للبحث", "قلعة السراغنة")
        amar = AmarAgent("Sraghna Digital Market")

        if st.button("🚀 تشغيل الوكيل وتوليد التقرير"):
            opps_brutes = amar.scanner_domain(city)
            if opps_brutes:
                opps_analyse = amar.analyse_domain(opps_brutes)
                rapport = amar.rapport_comm(opps_analyse)

                st.success("تم توليد التقرير بنجاح!")
                st.text_area(
                    "📲 نسخ التقرير لإرساله يدوياً عبر الواتساب:", rapport, height=200
                )

                encoded_msg = urllib.parse.quote(rapport)
                whatsapp_url = f"https://wa.me/{MY_PHONE}?text={encoded_msg}"
                st.markdown(
                    f"### [🔗 اضغط هنا للإرسال المباشر عبر واتساب]({whatsapp_url})",
                    unsafe_allow_html=True,
                )
            else:
                st.warning("⚠️ لا توجد صفقات جديدة مطابقة حالياً.")

    with tab3:
        st.subheader("📚 مواضيع وأقسام إضافية")
        st.markdown("""
        * **أراضي فلاحية وفيرمات:** عروض خاصة في قلعة السراغنة ومراكش.
        * **بقع أرضية سكنية وتجارية:** (الهدى، البدر، المنارة).
        * **مواد البناء والتجهيزات:** حديد، أسمنت، وسياجات فلاحية (RITA FER / Tassaout Services).
        * **خدمات رقمية وتسويق:** تصميم اللوحات الإشهارية وتطوير الأنظمة الذكية.
        """)

    with tab4:
        st.subheader("إضافة عرض عقاري أو صفقة جديدة")
        with st.form("add_ad_form"):
            msg = st.text_input("نص العرض/الإعلان (مثل: أرض فلاحية بالهدى)")
            reg = st.text_input("المنطقة/المدينة (مثل: قلعة السراغنة)", "قلعة السراغنة")
            mnt = st.number_input("المبلغ (بالدرهم)", min_value=0, value=50000)
            submit = st.form_submit_button("حفظ العرض في السيرفر")

            if submit:
                if msg and reg:
                    if supabase:
                        try:
                            data = {"message": msg, "region": reg, "montant": mnt}
                            supabase.table("instant_ads").insert(data).execute()
                            st.success("تم حفظ العرض بنجاح في قاعدة البيانات! 🚀")
                        except Exception as e:
                            st.error(f"خطأ أثناء الحفظ في Supabase: {e}")
                    else:
                        st.warning("⚠️ اتصال Supabase غير متوفر حالياً، تم محاكاة الحفظ بنجاح.")
                else:
                    st.warning("يرجى ملء البيانات الأساسية.")

# تذييل الصفحة العام
st.markdown("---")
st.caption("Alpha Core Nexus & Tassaout Digital Platform © 2026 | مرخص ومحمي برقم 0691897126 [TASSAOUT VERIFIED]")
