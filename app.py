import streamlit as st
from multi_domain_agent import MultiDomainAgent

# 1. إعدادات الصفحة والهوية البصرية للنظام
st.set_page_config(
    page_title="TASSAOUT OMEGA OS v2.0", 
    page_icon="🌐", 
    layout="wide"
)

# 2. تهيئة "العقل المدبر" في الجلسة لمنع إعادة التحميل
if 'brain' not in st.session_state:
    st.session_state.brain = MultiDomainAgent()

# 3. لوحة التحكم الجانبية (Sidebar)
with st.sidebar:
    st.title("🎯 TASSAOUT OMEGA")
    st.markdown("### *Omega OS v2.0*")
    st.markdown("---")
    
    selected_domain = st.selectbox(
        "اختر الوكيل النشط:",
        ["Marketing", "RealEstate", "Operations", "ImageEngine"]
    )
    
    st.markdown("---")
    if st.button("🔄 إعادة تهيئة المحرك", use_container_width=True):
        st.session_state.brain = MultiDomainAgent()
        st.success("تمت إعادة التهيئة بنجاح")
        
    st.info("نظام التشغيل الذكي جاهز لإدارة العمليات والعقارات.")
    st.success("الحالة: متصل ✅")

# 4. الواجهة الرئيسية
st.header("🌐 TASSAOUT OMEGA OS v2.0")
st.markdown("### *Super Multi-Domain Agentic AI OS*")
st.markdown("---")

# تقسيم الواجهة إلى تبويبات احترافية
tab1, tab2 = st.tabs(["🚀 لوحة التحكم والتشغيل", "📋 سجل العمليات (Logs)"])

with tab1:
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.subheader("منطقة الأوامر والتوجيه")
        user_input = st.text_area(
            "أدخل تعليماتك للعقل المدبر:", 
            height=200, 
            placeholder="مثال: قم بإنشاء إعلان تسويقي لقطعة أرض في قلعة السراغنة أو تحليل هوامش الربح..."
        )
        
        if st.button("🚀 تنفيذ المهمة عبر الوكيل", use_container_width=True, type="primary"):
            if user_input:
                with st.spinner("جاري المعالجة بواسطة OMEGA CORE..."):
                    # استدعاء العقل المدبر لتوجيه الطلب
                    result = st.session_state.brain.route_request(user_input, selected_domain)
                    
                    # محاولة حفظ السجل تلقائياً إذا كانت الدالة متوفرة
                    if hasattr(st.session_state.brain, 'log_to_file'):
                        st.session_state.brain.log_to_file(selected_domain, user_input, result)
                    
                    st.success("تم التنفيذ بنجاح!")
                    st.markdown("### 📊 النتيجة:")
                    st.code(result, language='markdown')
                    
                    # زر تحميل النتيجة مباشرة
                    st.download_button(
                        label="📥 تحميل النتيجة كملف نصي",
                        data=result,
                        file_name=f"Result_{selected_domain}.txt",
                        mime="text/plain"
                    )
            else:
                st.warning("يرجى كتابة تعليماتك أولاً قبل التشغيل.")

    with col2:
        st.subheader("📊 لوحة المؤشرات")
        st.metric(label="حالة النظام", value="Online", delta="Operational")
        st.metric(label="الوكلاء النشطين", value="4")
        st.write("---")
        st.markdown("**أدوار الوكلاء المعتمدين:**")
        st.caption("- 📢 **Marketing:** تسويق وحملات رقمية\n- 🏠 **RealEstate:** إدارة العقارات والتجزئات\n- ⚙️ **Operations:** الأتمتة والسيرفرات\n- 🎨 **ImageEngine:** معالجة بصرية بريميوم")

with tab2:
    st.subheader("سجل العمليات والطلبات (System Logs)")
    st.caption("يتم تسجيل كافة العمليات والنتائج تلقائياً في الملف الخلفي للنظام.")
    
    if st.button("🔄 تحديث السجل"):
        st.rerun()
        
    try:
        with open("system_logs.txt", "r", encoding="utf-8") as f:
            log_content = f.read()
            if log_content.strip():
                st.text_area("محتويات سجل النظام:", log_content, height=350)
            else:
                st.info("السجل فارغ حالياً. قم بتنفيذ مهمة جديدة لتبدأ الأرشفة.")
    except FileNotFoundError:
        st.info("لم يتم العثور على ملف السجلات بعد. سيتم إنشاؤه تلقائياً مع أول عملية تنفيذ.")

# 5. التذييل (Footer)
st.markdown("---")
st.markdown("<center>Powered by <b>Alpha Core Nexus</b> | TASSAOUT OMEGA OS v2.0 | صنع في المغرب 🇲🇦</center>", unsafe_allow_html=True)
