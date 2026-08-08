from datetime import datetime
import io
import os
import urllib.parse
import zipfile
from PIL import Image, ImageEnhance
import streamlit as st

st.set_page_config(page_title="TASSAOUT OMEGA OS", page_icon="👑", layout="wide")
GALLERY_FOLDER = "gallery"
os.makedirs(GALLERY_FOLDER, exist_ok=True)

CORE_DB = {
    "sectors": ["عقار", "سيارات", "فلاحة", "مواد إنشائية"],
    "cities": ["مراكش", "قلعة السراغنة", "الدار البيضاء", "أكادير", "طنجة"],
    "tech": {
        "عقار": "Hasselblad X2D",
        "سيارات": "Sony A1",
        "فلاحة": "Phase One IQ4",
        "مواد إنشائية": "DJI Drone + Sony A1",
        "عام": "Universal Sensor",
    },
    "listings": {
        "عقار": [
            "أرض فلاحية 5 هكتارات بقلعة السراغنة - مجهزة ومحفيظة",
            "بقعة تجارية استراتيجية وسط مراكش - واجهة رئيسية",
            "منزل صفيحي/تجهيز سكني بقلعة السراغنة",
        ],
        "سيارات": [
            "شاحنة نقل بضائع دولية - حالة ممتازة موديل حديث",
            "سيارة نفعية رباعية الدفع - صيانة دورية",
        ],
        "فلاحة": [
            "تجهيز سقي قطرة الماء للأراضي الكبرى",
            "معدات حراثة رقمية متطورة",
        ],
    },
}

ENVIRONMENT_PRESETS = {
    "عقار فخم": {
        "camera": "Hasselblad X2D",
        "sharpness": 2.2,
        "contrast": 1.6,
        "color": 1.3,
    },
    "قطع غيار/سيارات": {
        "camera": "Sony A1",
        "sharpness": 1.9,
        "contrast": 1.8,
        "color": 1.2,
    },
    "مواد إنشائية/ميدان": {
        "camera": "Canon R5",
        "sharpness": 1.5,
        "contrast": 1.3,
        "color": 1.2,
    },
}


def apply_agentic_vision(image, preset):
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


xl_templates = {
    "عقار": lambda city, gear, details: (
        f"🏢 *تقرير معاينة عقارية - {city}*\n\n"
        f"📌 *العرض المعني:* {details}\n"
        f"🛠️ *تقنية التوثيق:* {gear}\n\n"
        "الوضع: المعاينة الميدانية مكتملة بدقة عالية.\n"
        "التقييم البصري والتقني متوافق مع معايير Sraghna Immobilière.\n"
        "جاهز لإتمام الصفقة أو العرض."
    ),
    "سيارات": lambda city, gear, details: (
        f"🚛 *تقرير حالة المركبة والآليات - {city}*\n\n"
        f"📌 *العرض المعني:* {details}\n"
        f"🛠️ *تقنية التوثيق:* {gear}\n\n"
        "الوضع: تم التحقق من الحالة العامة والمواصفات.\n"
        "التقرير الفني: ممتاز ومطابق للمعايير المطلوبة."
    ),
    "فلاحة": lambda city, gear, details: (
        f"🚜 *تقرير المسح الفلاحي الميداني - {city}*\n\n"
        f"📌 *العرض المعني:* {details}\n"
        f"🛠️ *تقنية التوثيق:* {gear}\n\n"
        "الوضع: تم مسح الحدود والتوثيق البصري.\n"
        "الاستراتيجية: الأرض جاهزة للاستغلال والتطوير الاستثماري."
    ),
}

if "last_action" not in st.session_state:
  st.session_state["last_action"] = "System Idle"

st.title("👑 TASSAOUT OMEGA OS | Sraghna Immobilière")
st.sidebar.success("System Status: Online ✅")
st.sidebar.metric("الصور المؤرشفة ميدانياً", len(os.listdir(GALLERY_FOLDER)))

tab1, tab2, tab3 = st.tabs(
    [
        "📸 التصوير أو تحميل الصور",
        "🧠 عروض الوكيل والتفاعل",
        "📦 الأرشيف",
    ]
)

with tab1:
  st.subheader("📷 مركز الوسائط: التقاط بالكاميرا أو رفع صورة جاهزة")

  col1, col2 = st.columns(2)
  with col1:
    selected_env = st.selectbox(
        "اختر بيئة التوثيق:", list(ENVIRONMENT_PRESETS.keys())
    )
  with col2:
    selected_sector = st.selectbox(
        "اختر القطاع للتوثيق:", CORE_DB["sectors"]
    )

  current_preset = ENVIRONMENT_PRESETS.get(
      selected_env, list(ENVIRONMENT_PRESETS.values())[0]
  )

  upload_option = st.radio(
      "اختر طريقة إدخال الصورة:",
      ["التقاط صورة مباشرة بالكاميرا", "تحميل صورة من الجهاز/الهاتف"],
  )

  image_to_process = None

  if upload_option == "التقاط صورة مباشرة بالكاميرا":
    photo = st.camera_input("📷 التقط المشهد بوضوح")
    if photo:
      image_to_process = Image.open(photo)
  else:
    uploaded_file = st.file_uploader(
        "📁 اختر أو اسحب صورة العقار/الآلية هنا", type=["jpg", "jpeg", "png"]
    )
    if uploaded_file:
      image_to_process = Image.open(uploaded_file)

  if image_to_process:
    processed_image = apply_agentic_vision(image_to_process, current_preset)
    image_path = save_to_gallery(processed_image, selected_env)
    st.image(
        processed_image,
        caption=(
            f"✅ تمت المعالجة بنجاح عبر عدسة الاحتراف"
            f" {current_preset['camera']}"
        ),
        use_container_width=True,
    )
    st.success("تم حفظ الصورة في الأرشيف الميداني بنجاح.")

with tab2:
  st.subheader("🧠 عروض النظام والتحكم المباشر (Sraghna Immobilière)")

  active_sector = st.selectbox(
      "حدد القطاع لاستعراض عروضه:", CORE_DB["sectors"], key="sec_listings"
  )
  available_listings = CORE_DB["listings"].get(
      active_sector, ["عروض عامة ومتاحة في المنظومة"]
  )
  selected_listing = st.selectbox(
      "📋 العروض العقارية والتجارية المتاحة حالياً:", available_listings
  )

  selected_city = st.selectbox("المدينة المعنية:", CORE_DB["cities"])

  user_input = st.text_area(
      "أمر الوكيل الذكي (TASSAOUT MEGA GO):",
      value=(
          f"TASSAOUT MEGA GO {active_sector} {selected_city} -"
          f" {selected_listing}"
      ),
      height=90,
  )

  if st.button("🚀 توليد التقرير الاحترافي وإعداده للواتساب"):
    gear = CORE_DB["tech"].get(active_sector, "Universal Sensor")
    generator = xl_templates.get(
        active_sector,
        lambda c, g, d: (
            f"📌 *تقرير ميداني - {c}*\nالعرض: {d}\nتم التوثيق بواسطة"
            f" *{g}*.\nالحالة: جاهز."
        ),
    )
    report_text = generator(selected_city, gear, selected_listing)
    st.session_state["last_action"] = report_text

    st.success("🎯 تم توليد التقرير بنجاح!")
    st.code(report_text, language="markdown")

    whatsapp_number = "212691897126"
    encoded_text = urllib.parse.quote(report_text)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_text}"
    st.link_button(
        "📱 إرسال التقرير فوراً عبر الواتساب (شغال 100%)", whatsapp_url
    )

with tab3:
  st.subheader("📦 الأرشيف الذكي للصور والتقارير")
  if st.button("📦 تحميل حزمة الأرشيف الكاملة (ZIP)"):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
      for file in os.listdir(GALLERY_FOLDER):
        zip_file.write(os.path.join(GALLERY_FOLDER, file), file)
    st.download_button(
        "⬇️ تحميل الأرشيف البرمجي والميداني",
        data=zip_buffer.getvalue(),
        file_name=f"ARCHIVE_SRAGHNA_{datetime.now().strftime('%Y-%m-%d')}.zip",
    )
