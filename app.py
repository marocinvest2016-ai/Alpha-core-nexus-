from datetime import datetime
import io
import os
import zipfile
import pandas as pd
from PIL import Image, ImageEnhance
import streamlit as st

# 1. إعدادات النظام السيادي والهوية البصرية
st.set_page_config(
    page_title="TASSAOUT OMEGA OS - Unified Core", page_icon="👑", layout="wide"
)

st.title("👑 TASSAOUT OMEGA OS | Unified Intelligence Core")
st.markdown("### *السوبر وكيل المتعدد المجالات - عقل الكاميرا والبيانات الذكي*")
st.markdown("---")

GALLERY_FOLDER = "gallery"
os.makedirs(GALLERY_FOLDER, exist_ok=True)

# 2. الكبسولة التكنولوجية: محرك اختيار العدسات والبيئات بذكاء الوكيل
ENVIRONMENT_PRESETS = {
    "عقار فخم (مراكش)": {
        "camera": "Hasselblad X2D 100C",
        "lens": "38mm f/2.5 V",
        "sharpness": 2.2,
        "contrast": 1.6,
        "color": 1.3,
        "agent_role": "RealEstate & Marketing Agent",
        "logic": (
            "إبراز التفاصيل المعمارية، الألوان الدافئة، وإعداد الإعلان التسويقي"
            " المرافق."
        ),
    },
    "تجزئة أرضية (قلعة السراغنة)": {
        "camera": "Sony A1 Professional",
        "lens": "24-70mm f/2.8 GM II",
        "sharpness": 1.8,
        "contrast": 1.9,
        "color": 1.4,
        "agent_role": "Topography & Operations Agent",
        "logic": (
            "توضيح التضاريس، الخطوط الحدية للأراضي، وحساب هوامش الربح التقريبية"
            " للمشروع."
        ),
    },
    "توثيق ميداني وسريع": {
        "camera": "Canon EOS R5",
        "lens": "50mm f/1.2L",
        "sharpness": 1.5,
        "contrast": 1.3,
        "color": 1.2,
        "agent_role": "General Operations Agent",
        "logic": "ضبط الإضاءة السريعة، الحفاظ على الواقعية، وأرشفة الملفات تلقائياً.",
    },
}


def apply_agentic_vision(image, preset):
  """تطبيق معالجة ذكية للصورة بناءً على إعدادات الوكيل البيئي"""
  enhancer = ImageEnhance.Sharpness(image)
  image = enhancer.enhance(preset["sharpness"])
  enhancer = ImageEnhance.Contrast(image)
  image = enhancer.enhance(preset["contrast"])
  enhancer = ImageEnhance.Color(image)
  image = enhancer.enhance(preset["color"])
  return image


def save_to_gallery(image, env_name):
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  filename = (
      f"{GALLERY_FOLDER}/MEGA_{timestamp}_{env_name.replace(' ', '_')}.jpg"
  )
  image.save(filename, quality=95)
  return filename


# 3. قاعدة بيانات الكاميرات الـ 100
CAMERAS_100 = [
    # Canon 1-8
    {"id": 1, "brand": "Canon", "name": "EOS R5", "type": "Hybride 8K"},
    {"id": 2, "brand": "Canon", "name": "EOS R3", "type": "Pro sport"},
    {
        "id": 3,
        "brand": "Canon",
        "name": "EOS 5D Mark IV",
        "type": "Référence plein format",
    },
    {
        "id": 4,
        "brand": "Canon",
        "name": "EOS 1DX Mark III",
        "type": "Photojournalisme",
    },
    {"id": 5, "brand": "Canon", "name": "C70", "type": "Cinéma"},
    {"id": 6, "brand": "Canon", "name": "EOS M50", "type": "Vlog"},
    {"id": 7, "brand": "Canon", "name": "AE-1", "type": "Argentique culte"},
    {"id": 8, "brand": "Canon", "name": "7D Mark II", "type": "APS-C sport"},
    # Nikon 9-16
    {"id": 9, "brand": "Nikon", "name": "Z9", "type": "Flagship 8K"},
    {"id": 10, "brand": "Nikon", "name": "Z8", "type": "Z9 compact"},
    {
        "id": 11,
        "brand": "Nikon",
        "name": "D850",
        "type": "Roi du détail 45MP",
    },
    {"id": 12, "brand": "Nikon", "name": "D6", "type": "Pro sport"},
    {"id": 13, "brand": "Nikon", "name": "Z6 III", "type": "Hybride polyvalent"},
    {"id": 14, "brand": "Nikon", "name": "F3", "type": "Argentique légendaire"},
    {"id": 15, "brand": "Nikon", "name": "F2", "type": "Mécanique indestructible"},
    {"id": 16, "brand": "Nikon", "name": "D500", "type": "APS-C référence"},
    # Sony 17-24
    {"id": 17, "brand": "Sony", "name": "A1", "type": "50MP + 30fps"},
    {"id": 18, "brand": "Sony", "name": "A9 III", "type": "Obturateur global"},
    {"id": 19, "brand": "Sony", "name": "A7R V", "type": "61MP paysage"},
    {"id": 20, "brand": "Sony", "name": "A7 IV", "type": "Hybride best-seller"},
    {"id": 21, "brand": "Sony", "name": "FX3", "type": "Cinéma compact"},
    {"id": 22, "brand": "Sony", "name": "FX6", "type": "Doc/Ciné"},
    {"id": 23, "brand": "Sony", "name": "A6700", "type": "APS-C vidéo"},
    {"id": 24, "brand": "Sony", "name": "RX100 VII", "type": "Compact expert"},
    # Fujifilm 25-30
    {"id": 25, "brand": "Fujifilm", "name": "X-T5", "type": "40MP + look film"},
    {"id": 26, "brand": "Fujifilm", "name": "X-H2S", "type": "Sport/vidéo"},
    {
        "id": 27,
        "brand": "Fujifilm",
        "name": "GFX 100S II",
        "type": "Moyen format 100MP",
    },
    {
        "id": 28,
        "brand": "Fujifilm",
        "name": "X100VI",
        "type": "Compact télémétrique",
    },
    {"id": 29, "brand": "Fujifilm", "name": "X-S20", "type": "Vlog"},
    {"id": 30, "brand": "Fujifilm", "name": "Instax", "type": "Instantané"},
    # Panasonic / Leica 31-36
    {
        "id": 31,
        "brand": "Panasonic",
        "name": "Lumix S5 IIX",
        "type": "6K C-Log3",
    },
    {"id": 32, "brand": "Panasonic", "name": "GH6", "type": "Micro 4/3 vidéo"},
    {"id": 33, "brand": "Panasonic", "name": "S1R", "type": "47MP"},
    {
        "id": 34,
        "brand": "Leica",
        "name": "M11",
        "type": "Télémétrique plein format",
    },
    {"id": 35, "brand": "Leica", "name": "Q3", "type": "Compact 60MP"},
    {"id": 36, "brand": "Leica", "name": "SL3", "type": "Hybride luxe"},
    # RED / ARRI / Blackmagic 37-42
    {"id": 37, "brand": "RED", "name": "V-RAPTOR 8K", "type": "Cinéma"},
    {"id": 38, "brand": "RED", "name": "KOMODO 6K", "type": "Compact cinéma"},
    {"id": 39, "brand": "ARRI", "name": "Alexa 35", "type": "Référence cinéma"},
    {
        "id": 40,
        "brand": "ARRI",
        "name": "Alexa Mini LF",
        "type": "Cinéma grand format",
    },
    {"id": 41, "brand": "Blackmagic", "name": "URSA 12K", "type": "Cinéma"},
    {"id": 42, "brand": "Blackmagic", "name": "Pocket 6K Pro", "type": "Indé"},
    # Kodak 43-46
    {"id": 43, "brand": "Kodak", "name": "Pixpro AZ528", "type": "Bridge"},
    {
        "id": 44,
        "brand": "Kodak",
        "name": "M35",
        "type": "Argentique rechargeable",
    },
    {"id": 45, "brand": "Kodak", "name": "Ektar H35", "type": "Demi-format"},
    {"id": 46, "brand": "Kodak", "name": "Super 8 C70", "type": "Caméra film"},
    # Olympus / OM 47-49
    {
        "id": 47,
        "brand": "OM System",
        "name": "OM-1 Mark II",
        "type": "Micro 4/3 pro",
    },
    {"id": 48, "brand": "OM System", "name": "OM-5", "type": "Aventure"},
    {"id": 49, "brand": "Olympus", "name": "PEN-F", "type": "Retro"},
    # Hasselblad 50-52
    {
        "id": 50,
        "brand": "Hasselblad",
        "name": "X2D 100C",
        "type": "Moyen format 100MP",
    },
    {"id": 51, "brand": "Hasselblad", "name": "907X", "type": "Modulaire"},
    {
        "id": 52,
        "brand": "Hasselblad",
        "name": "500C/M",
        "type": "Argentique lunaire",
    },
    # Phase One 53-54
    {
        "id": 53,
        "brand": "Phase One",
        "name": "XF IQ4 150MP",
        "type": "Studio ultime",
    },
    {"id": 54, "brand": "Phase One", "name": "XT", "type": "Paysage technique"},
    # GoPro / DJI 55-57
    {"id": 55, "brand": "GoPro", "name": "Hero 12", "type": "Action"},
    {"id": 56, "brand": "DJI", "name": "Osmo Pocket 3", "type": "Vlog stabilisé"},
    {"id": 57, "brand": "DJI", "name": "Action 4", "type": "Action"},
    # Pentax / Ricoh 58-60
    {"id": 58, "brand": "Pentax", "name": "K-3 Mark III", "type": "Reflex APS-C"},
    {"id": 59, "brand": "Pentax", "name": "645Z", "type": "Moyen format"},
    {"id": 60, "brand": "Ricoh", "name": "GR III", "type": "Compact street"},
    # Autres 61-100
    {
        "id": 61,
        "brand": "Contax",
        "name": "T3",
        "type": "Compact argentique luxe",
    },
    {"id": 62, "brand": "Contax", "name": "645", "type": "Moyen format"},
    {"id": 63, "brand": "Yashica", "name": "Mat-124", "type": "TLR"},
    {"id": 64, "brand": "Mamiya", "name": "RZ67", "type": "Studio moyen format"},
    {
        "id": 65,
        "brand": "Mamiya",
        "name": "7 II",
        "type": "Télémétrique moyen format",
    },
    {"id": 66, "brand": "Bronica", "name": "SQ-A", "type": "6x6"},
    {"id": 67, "brand": "Rollei", "name": "35", "type": "Mini argentique"},
    {
        "id": 68,
        "brand": "Polaroid",
        "name": "SX-70",
        "type": "Instantané pliable",
    },
    {"id": 69, "brand": "Polaroid", "name": "Now+", "type": "Instantané moderne"},
    {"id": 70, "brand": "Lomo", "name": "LC-A", "type": "Lo-fi"},
    {"id": 71, "brand": "Holga", "name": "120", "type": "Toy camera"},
    {"id": 72, "brand": "Diana", "name": "F+", "type": "Toy camera"},
    {"id": 73, "brand": "Sigma", "name": "fp L", "type": "Plein format compact"},
    {"id": 74, "brand": "Sigma", "name": "sd Quattro", "type": "Foveon"},
    {"id": 75, "brand": "Panasonic", "name": "S9", "type": "Compact plein format"},
    {"id": 76, "brand": "Canon", "name": "EOS R50", "type": "Débutant"},
    {"id": 77, "brand": "Nikon", "name": "Zf", "type": "Retro numérique"},
    {"id": 78, "brand": "Sony", "name": "ZV-E10", "type": "Vlog APS-C"},
    {
        "id": 79,
        "brand": "Fujifilm",
        "name": "X-E4",
        "type": "Compact rangefinder",
    },
    {"id": 80, "brand": "Leica", "name": "D-Lux 8", "type": "Compact expert"},
    {"id": 81, "brand": "Panasonic", "name": "G9 II", "type": "Sport M4/3"},
    {
        "id": 82,
        "brand": "Canon",
        "name": "EOS R8",
        "type": "Plein format abordable",
    },
    {"id": 83, "brand": "Nikon", "name": "Z50 II", "type": "APS-C"},
    {"id": 84, "brand": "Sony", "name": "A7C II", "type": "Compact plein format"},
    {"id": 85, "brand": "Fujifilm", "name": "X-T50", "type": "Retro 40MP"},
    {"id": 86, "brand": "OM System", "name": "OM-3", "type": "Compact pro"},
    {"id": 87, "brand": "Hasselblad", "name": "503CW", "type": "Argentique pro"},
    {"id": 88, "brand": "RED", "name": "RAVEN", "type": "Cinéma 4.5K"},
    {"id": 89, "brand": "ARRI", "name": "416", "type": "16mm film"},
    {"id": 90, "brand": "Blackmagic", "name": "4K Production", "type": "Studio"},
    {"id": 91, "brand": "Kodak", "name": "Retina", "type": "Argentique vintage"},
    {"id": 92, "brand": "Nikon", "name": "FM2", "type": "Mécanique culte"},
    {"id": 93, "brand": "Canon", "name": "F-1", "type": "Pro argentique"},
    {
        "id": 94,
        "brand": "Sony",
        "name": "RX1R II",
        "type": "Compact plein format 35mm",
    },
    {"id": 95, "brand": "Leica", "name": "S3", "type": "Moyen format reflex"},
    {"id": 96, "brand": "Phase One", "name": "iXM", "type": "Aérien"},
    {"id": 97, "brand": "DJI", "name": "Ronin 4D", "type": "Caméra + nacelle"},
    {"id": 98, "brand": "Insta360", "name": "X4", "type": "360°"},
    {"id": 99, "brand": "Panasonic", "name": "BS1H", "type": "Box cinéma"},
    {
        "id": 100,
        "brand": "Canon",
        "name": "ME20F-SH",
        "type": "Low light monstre",
    },
]
df_cameras = pd.DataFrame(CAMERAS_100)

# 4. الواجهة الرئيسية بنظام التبويبات الشاملة
tab1, tab2, tab3, tab4 = st.tabs([
    "📸 الكاميرا الذكية (MEGA PREMIUM)",
    "🧠 محرك السوبر وكيل (Agentic Core)",
    "🗂️ قاعدة بيانات الـ 100 كاميرا",
    "📦 أرشيف السيرفر",
])

with tab1:
  st.subheader("الكاميرا الذكية ذاتية التوجيه")
  selected_env = st.selectbox(
      "اختر بيئة التصوير والهدف الميداني (سيقوم الوكيل بضبط العدسة تلقائياً):",
      list(ENVIRONMENT_PRESETS.keys()),
  )
  current_preset = ENVIRONMENT_PRESETS[selected_env]

  st.info(
      f"🤖 **الوكيل المسؤول:** {current_preset['agent_role']} \n\n 📷"
      f" **الكاميرا المخصصة:** {current_preset['camera']} | **العدسة:**"
      f" {current_preset['lens']}"
  )
  st.caption(f"💡 **استراتيجية المعالجة:** {current_preset['logic']}")
  st.markdown("---")

  photo = st.camera_input("📷 التقاط الصورة الميدانية عبر الكاميرا")
  if photo:
    raw_image = Image.open(photo)
    with st.spinner("جاري معالجة الصورة وتحليلها عبر السوبر وكيل البصري..."):
      processed_image = apply_agentic_vision(raw_image, current_preset)
      saved_path = save_to_gallery(processed_image, selected_env)

    st.success(f"✅ تم التقاط وتأكيد الصورة بنجاح وتخزينها في: `{saved_path}`")
    st.image(
        processed_image,
        caption=(
            f"البيئة: {selected_env} | الكاميرا: {current_preset['camera']}"
        ),
        use_column_width=True,
    )

    st.markdown("### 📝 تقرير الوكيل المرافق للصورة:")
    st.code(
        f"""
[TASSAOUT MEGA REPORT]
- البيئة المستهدفة: {selected_env}
- العتاد البصري: {current_preset['camera']}
- الحالة: تم التوثيق والمعالجة بنجاح لصالح مشاريع قلعة السراغنة ومراكش.
- الإجراء الموالي: جاهز للإدراج في الحملات أو حساب هوامش التجزئة.
        """,
        language="markdown",
    )

with tab2:
  st.subheader("🧠 محرك السوبر وكيل (Powered by Agentic Logic)")
  st.write(
      "هنا يتم إدارة التوجيهات البرمجية والمهام الميدانية المتقدمة المرتبطة"
      " بنظام Sraghna Immobilière:"
  )

  agent_task = st.selectbox(
      "اختر المهمة الميدانية:",
      [
          "تحليل صورة عقارية",
          "توليد تقرير استثماري",
          "بحث متقدم في قواعد البيانات",
      ],
  )
  user_query = st.text_area(
      "أدخل تعليماتك الخاصة بهذا المجال:",
      placeholder="مثال: جهز لي تقرير بصري وتسويقي لأرض في الهدا...",
  )

  if st.button("تفعيل ذكاء الوكيل"):
    with st.spinner("جاري التواصل مع محرك الاستدلال الذكي..."):
      st.write(f"✅ تم تفعيل المهمة: **{agent_task}** بنجاح.")
      st.info(
          "الوكيل يقوم الآن بمعالجة البيانات الميدانية وتحليل المدخلات الخاصة"
          " بـ قلعة السراغنة ومراكش..."
      )
      st.code(
          f"""
[AGENT EXECUTION LOG]
- المهمة المنفذة: {agent_task}
- النص المدخل: {user_query if user_query else 'عمليات روتينية تلقائية'}
- الحالة: جاهز لربط مخرجات النماذج المتقدمة (Awesome LLM Apps) والتعامل مع الأرشيف.
            """,
          language="markdown",
      )

with tab3:
  st.subheader("🗂️ قاعدة بيانات الكاميرات الشاملة (100 كاميرا)")
  st.markdown("نظام إدارة وتحليل قاعدة بيانات الكاميرات الاحترافية")

  selected_brand = st.selectbox(
      "اختر العلامة التجارية (Brand)",
      ["الكل"] + sorted(df_cameras["brand"].unique().tolist()),
      key="cam_brand_filter",
  )
  search_query = st.text_input(
      "بحث بالاسم أو النوع", key="cam_search_input"
  )

  filtered_df = df_cameras.copy()
  if selected_brand != "الكل":
    filtered_df = filtered_df[filtered_df["brand"] == selected_brand]
  if search_query:
    filtered_df = filtered_df[
        filtered_df["name"].str.contains(search_query, case=False, na=False)
        | filtered_df["type"].str.contains(search_query, case=False, na=False)
    ]

  col1, col2, col3 = st.columns(3)
  col1.metric("إجمالي الكاميرات المتاحة", len(df_cameras))
  col2.metric("العلامات التجارية", df_cameras["brand"].nunique())
  col3.metric("النتائج المعروضة بعد الفلترة", len(filtered_df))

  st.markdown("---")
  st.dataframe(filtered_df, use_container_width=True)

with tab4:
  st.subheader("📦 الأرشيف الذكي والروابط الأسبوعية")
  if st.button("📦 توليد حزمة الأرشيف ZIP"):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
      if os.path.exists(GALLERY_FOLDER):
        for file in os.listdir(GALLERY_FOLDER):
          zip_file.write(os.path.join(GALLERY_FOLDER, file), file)

    st.download_button(
        label="⬇️ تحميل الأرشيف الكامل للصوّر والتقارير",
        data=zip_buffer.getvalue(),
        file_name=(
            f"TASSAOUT_MEGA_ARCHIVE_{datetime.now().strftime('%Y-%m-%d')}.zip"
        ),
        mime="application/zip",
    )
    st.warning("⚠️ الأرشيف متاح للتحميل الفوري.")

    whatsapp_url = "https://wa.me/?text=تقرير+وكيل+تاساوت+ميغا+بريميوم+جاهز"
    st.link_button("📱 مشاركة التقرير عبر الواتساب", whatsapp_url)

# الـ Sidebar الخاص بالنظام الموحد
st.sidebar.markdown("### 🌐 سيادة النظام")
st.sidebar.success("MEGA PREMIUM: Online ✅")
st.sidebar.metric(
    "عدد الصور المؤرشفة",
    len(os.listdir(GALLERY_FOLDER)) if os.path.exists(GALLERY_FOLDER) else 0,
)
st.sidebar.markdown("---")
st.sidebar.caption(
    "TASSAOUT OMEGA OS v2.0 - صُمم خصيصاً للريادة في مراكش وقلعة السراغنة 🇲🇦"
)
