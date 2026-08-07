import streamlit as st
from datetime import datetime

# إعداد النظام
st.set_page_config(page_title="TASSAOUT OMEGA OS", layout="wide")

# قاعدة المعرفة الدائمة للوكيل (مخفية عن المستخدم)
CORE_DB = {
    "sectors": ["عقار", "سيارات", "خدمات", "تسويق", "فلاحة", "لوجستيك", "تعاونيات"],
    "cities": ["مراكش", "قلعة السراغنة", "الدار البيضاء", "أكادير", "طنجة"],
    "tech": {"عقار": "Hasselblad", "سيارات": "Sony A1", "فلاحة": "Phase One"}
}

# حالة النظام (Persistence)
if 'last_action' not in st.session_session:
    st.session_session['last_action'] = "System Idle - Monitoring All Sectors..."

# واجهة النظام (تعمل للجميع)
st.title("🌐 TASSAOUT OMEGA OS | Unified Operations")
st.sidebar.success("System Status: Online & Monitoring ✅")

# التفاعل الذكي
user_input = st.text_area("مركز القيادة الميداني:", placeholder="اكتب تعليماتك هنا...")

if st.button("إرسال التعليمات"):
    if "TASSAOUT MEGA GO" in user_input.upper():
        # هنا يتفاعل الوكيل معك فقط
        sector = next((s for s in CORE_DB["sectors"] if s in user_input), "عام")
        city = next((c for c in CORE_DB["cities"] if c in user_input), "المغرب")
        gear = CORE_DB["tech"].get(sector, "Universal Sensor")
        
        response = f"🎯 [MEGA COMMAND ACTIVE] \n- القطاع: {sector} \n- النطاق: {city} \n- الكاميرا المختارة (خلفية): {gear} \n- الإجراء: تنفيذ البرومبت فوراً وتجهيز المخرجات."
        st.session_session['last_action'] = response
        st.success(response)
    else:
        # هنا يعمل الوكيل في الخلفية لخدمة الجميع
        st.info("🔄 الوكيل يعمل في الخلفية على معالجة العمليات العامة...")
        st.write("الطلب مسجل في سجل المهام العام للوكيل.")

# عرض آخر تحديث للعمليات
st.markdown("---")
st.subheader("سجل العمليات النشط:")
st.text(st.session_session['last_action'])
