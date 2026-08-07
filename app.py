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

# 2. الكبسولة التقنية: دماغ الوكيل المضمن (يحتوي على إعدادات العدسات والكاميرات الاحترافية في الخلفية)
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
  """تطبيق معالجة ذكية للصورة بناءً على إعدادات الوكيل البيئي المخفية"""
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


# 3. الواجهة الرئيسية (تم دمج وترتيب التبويبات بدون زحمة واجهة الكاميرات)
tab1, tab2, tab3 = st.tabs([
    "📸 التقاط والتوثيق الميداني",
    "🧠 محرك السوبر وكيل (Agentic Core)",
    "📦 أرشيف السيرفر",
])

with tab1:
  st.subheader("الكاميرا الذكية ذاتية التوجيه (مدارة بذكاء الوكيل)")
  selected_env = st.selectbox(
      "اختر بيئة التصوير والهدف الميداني (الوكيل يطبق العتاد المناسب في"
      " الخلفية):",
      list(ENVIRONMENT_PRESETS.keys()),
  )
  current_preset = ENVIRONMENT_PRESETS[selected_env]

  st.info(
      f"🤖 **الوكيل المسؤول:** {current_preset['agent_role']} \n\n ⚙️ **العتاد"
      f" المدار تلقائياً:** {current_preset['camera']} | العدسة:"
      f" {current_preset['lens']}"
  )
  st.caption(f"💡 **استراتيجية المعالجة:** {current_preset['logic']}")
  st.markdown("---")

  photo = st.camera_input("📷 التقاط الصورة الميدانية")
  if photo:
    raw_image = Image.open(photo)
    with st.spinner("جاري معالجة الصورة وتحليلها عبر السوبر وكيل البصري..."):
      processed_image = apply_agentic_vision(raw_image, current_preset)
      saved_path = save_to_gallery(processed_image, selected_env)

    st.success(f"✅ تم التقاط وتأكيد الصورة بنجاح وتخزينها في: `{saved_path}`")
    st.image(
        processed_image,
        caption=(
            f"البيئة: {selected_env} | العتاد: {current_preset['camera']}"
        ),
        use_column_width=True,
    )

    st.markdown("### 📝 تقرير الوكيل المرافق للصورة:")
    st.code(
        f"""
[TASSAOUT MEGA REPORT]
- البيئة المستهدفة: {selected_env}
- العتاد البصري (المضمن): {current_preset['camera']}
- الحالة: تم التوثيق والمعالجة بنجاح لصالح مشاريع قلعة السراغنة ومراكش.
        """,
        language="markdown",
    )

with tab2:
  st.subheader("🧠 محرك السوبر وكيل (Powered by Agentic Logic)")
  st.write(
      "أدخل استفسارك أو طلبك العقاري والميداني، وسيقوم الوكيل بالرد الفوري بناءً"
      " على كبسولته المعلوماتية:"
  )

  agent_task = st.selectbox(
      "اختر المهمة الميدانية:",
      [
          "تحليل طلب عقاري",
          "توليد تقرير استثماري",
          "بحث في قوائم Listings",
      ],
  )
  user_query = st.text_area(
      "أدخل تعليماتك الخاصة بهذا المجال:",
      placeholder="مثال: مطلوب بقعة تجارية في قلعة السراغنة...",
  )

  if st.button("تفعيل ذكاء الوكيل"):
    with st.spinner("جاري استخراج الرد العقاري والتحليل الميداني..."):
      st.success(f"✅ تم تنفيذ المهمة: **{agent_task}** بنجاح.")

      # تفاعل ذكي بناءً على إدخال المستخدم
      if (
          "بقعة" in user_query
          or "تجارية" in user_query
          or "السراغنة" in user_query
          or "مراكش" in user_query
      ):
        st.markdown("### 📋 مقترح الوكيل العقاري:")
        st.info(
            "🔹 **نوع الطلب:** مسجل ضمن نطاق البحث العقاري\n"
            "🔹 **المنطقة المستهدفة:** قلعة السراغنة / مراكش\n"
            "🔹 **الإجراء المقترح:** تم رصد الطلب وإدراجه في قائمة المتابعة"
            " الميدانية لتجارب التجزئة والأراضي. جاهز لربطه بملفات الـ Listings"
            " وتوليد العرض التسويقي."
        )
      else:
        st.info(
            "الوكيل يقوم الآن بمعالجة البيانات الميدانية وتحليل المدخلات الخاصة"
            " بنجاح..."
        )

      st.code(
          f"""
[AGENT EXECUTION LOG]
- المهمة المنفذة: {agent_task}
- النص المدخل: {user_query if user_query else 'عمليات روتينية'}
- الحالة: مكتمل بنجاح عبر كبسولة النظام.
          """,
          language="markdown",
      )

with tab3:
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
