from datetime import datetime
import io
import os
import urllib.parse
import zipfile
from PIL import Image, ImageEnhance
import streamlit as st

# 1. إعداد النظام السيادي
st.set_page_config(
    page_title="TASSAOUT OMEGA OS", page_icon="👑", layout="wide"
)
GALLERY_FOLDER = "gallery"
os.makedirs(GALLERY_FOLDER, exist_ok=True)

# 2. قاعدة المعرفة الدائمة للوكيل (موسعة ومغلقة)
CORE_DB = {
    "sectors": [
        "عقار",
        "سيارات",
        "خدمات",
        "تسويق",
        "فلاحة",
        "لوجستيك",
        "تعاونيات",
        "قطع غيار",
        "مواد إنشائية",
    ],
    "cities": ["مراكش", "قلعة السراغنة", "الدار البيضاء", "أكادير", "طنجة"],
    "tech": {
        "عقار": "Hasselblad X2D",
        "سيارات": "Sony A1",
        "فلاحة": "Phase One IQ4",
        "قطع غيار": "Canon R5",
        "مواد إنشائية": "DJI Drone + Sony A1",
        "عام": "Universal Sensor",
    },
}

# 3. دوال الكاميرا والتوثيق الذكي
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


# 4. قوالب التقارير الاحترافية المؤسساتية
xl_templates = {
    "عقار": lambda city, gear: (
        f"🏢 *تقرير معاينة عقارية - {city}*\nنؤكد لكم أننا قمنا بالمعاينة"
        f" الميدانية الدقيقة باستخدام تقنيات *{gear}*.\nالوضع: المعاينة مكتملة.\nالتقرير"
        " الفني: التقييم البصري والتقني متوافق مع معايير الجودة المعتمدة لدينا.\nنحن"
        " في خدمتكم لاتخاذ الخطوة التالية."
    ),
    "سيارات": lambda city, gear: (
        f"🚛 *تقرير حالة المركبة - {city}*\nتم توثيق حالة المركبة والتحقق من"
        f" المواصفات باستخدام *{gear}*.\nالتقرير الفني: الحالة العامة ممتازة"
        " ومطابقة للمواصفات المعلنة.\nلأي تفاصيل إضافية، فريقنا في خدمتكم."
    ),
    "فلاحة": lambda city, gear: (
        f"🚜 *تقرير التوثيق الميداني الفلاحي - {city}*\nتمت عملية المسح الميداني"
        f" للأراضي باستخدام *{gear}*.\nالتقرير الفني: المخططات والحدود موثقة"
        " ومتاحة للمراجعة.\nالاستراتيجية: جاهزون للتطوير والاستغلال الفلاحي."
    ),
}

# 5. حالة النظام
if "last_action" not in st.session_state:
  st.session_state["last_action"] = "System Idle - Monitoring All Sectors..."

# 6. واجهة المستخدم
st.title("👑 TASSAOUT OMEGA OS | Field Agent v3.0")
st.sidebar.success("System Status: Online & Monitoring ✅")
st.sidebar.metric("الصور المؤرشفة", len(os.listdir(GALLERY_FOLDER)))

tab1, tab2 = st.tabs(["📸 التوثيق الميداني + الوكيل", "📦 الأرشيف"])

with tab1:
  st.subheader("مركز القيادة الميداني")
  selected_env = st.selectbox(
      "اختر بيئة التوثيق:", list(ENVIRONMENT_PRESETS.keys())
  )
  current_preset = ENVIRONMENT_PRESETS[selected_env]

  user_input = st.text_area(
      "اكتب تعليماتك هنا:",
      placeholder="مثال: TASSAOUT MEGA GO عقار مراكش",
  )
  photo = st.camera_input("📷 أو التقط صورة للتوثيق")

  if st.button("تفعيل الوكيل وإرسال التقرير"):
    report_text = ""
    image_path = None

    if photo:
      raw_image = Image.open(photo)
      processed_image = apply_agentic_vision(raw_image, current_preset)
      image_path = save_to_gallery(processed_image, selected_env)
      st.image(
          processed_image,
          caption=f"تم التوثيق بـ {current_preset['camera']}",
          use_container_width=True,
      )

    if "TASSAOUT MEGA GO" in user_input.upper():
      sector = next((s for s in CORE_DB["sectors"] if s in user_input), "عام")
      city = next((c for c in CORE_DB["cities"] if c in user_input), "المغرب")
      gear = CORE_DB["tech"].get(sector, "Universal Sensor")

      # توليد التقرير الاحترافي حسب القطاع
      generator = xl_templates.get(
          sector,
          lambda c, g: (
              f"📌 *تقرير ميداني - {c}*\nتم التوثيق بواسطة *{g}*.\nالحالة: جاهز"
              " للمراجعة."
          ),
      )
      report_text = generator(city, gear)

      st.session_state["last_action"] = report_text
      st.success("✅ تم تفعيل أمر MEGA GO بنجاح")
    else:
      report_text = f"طلب عام مسجل: {user_input}"
      st.info("🔄 الطلب مسجل في سجل المهام العام")

    if report_text:
      whatsapp_number = "2126XXXXXXXX"  # ضع رقم هاتفك هنا بدون علامة +
      encoded_text = urllib.parse.quote(report_text)
      whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_text}"
      st.link_button("📱 إرسال التقرير للواتساب الآن", whatsapp_url)

with tab2:
  st.subheader("الأرشيف الذكي")
  if st.button("📦 توليد حزمة الأرشيف ZIP"):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zip_file:
      for file in os.listdir(GALLERY_FOLDER):
        zip_file.write(os.path.join(GALLERY_FOLDER, file), file)
    st.download_button(
        "⬇️ تحميل الأرشيف",
        data=zip_buffer.getvalue(),
        file_name=f"ARCHIVE_{datetime.now().strftime('%Y-%m-%d')}.zip",
    )
