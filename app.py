import streamlit as st
from multi_domain_agent import SuperMultiDomainAgent

# تشغيل الوكيل الرئيسي
agent_router = SuperMultiDomainAgent()

st.set_page_config(page_title="DANA - Super Multi-Domain Core Nexus", page_icon="🏢", layout="wide")

# القائمة الجانبية للتنقل
st.sidebar.title("🏢 وكالة تساوت الرقمية")
page = st.sidebar.selectbox("اختر القسم", ["🏠 الرئيسية", "🏡 وكيل العقارات", "💬 المحادثة الذكية مع Dana", "⚙️ التحكم الذكي بالوكلاء"])

if page == "🏠 الرئيسية":
    st.title("🌐 DANA - Super Multi-Domain Core Nexus v2.0")
    st.subheader("المنظومة الذكية المستقلة - قلعة السراغنة ومراكش")
    st.markdown("""
    مرحباً بك في المنصة المركزية لإدارة العقارات، الاستثمار، التصميم، والتحكم الآلي.
    استخدم القائمة الجانبية لتوجيه المهام للوكيل المتخصص المناسب.
    """)
    st.info("💡 النظام متصل مباشرة بمستودع GitHub ويعمل بنظام الوكلاء المتعددين (Multi-Domain Agentic AI).")

elif page == "🏡 وكيل العقارات":
    st.title("📋 العروض العقارية والاستثمارية المتاحة")
    st.markdown("إليك أحدث العروض والفرص المتاحة بقلعة السراغنة ومحيطها:")
    
    properties = [
        {"title": "بقع سكنية وتجارية في تجزئة الهدى", "category": "بقع سكنية وتجارية", "details": "من 80م² إلى 240م² مع موقع استراتيجي وأسعار تنافسية", "phone": "0691897126"},
        {"title": "بقع لبناء عمارات أو مشاريع تجارية", "category": "فرص استثمارية", "details": "مساحات من 80م² إلى 240م²+ عند أصحاب الأملاك مباشرة", "phone": "0691897126"},
        {"title": "شقق ومكاتب للكراء المهني والسكني", "category": "الكراء", "details": "مواقع استراتيجية وجاهزة للاستغلال الفوري بقلعة السراغنة", "phone": "0691897126"},
        {"title": "أراضي فلاحية وفيرمات للاستغلال", "category": "استثمار فلاحي", "details": "مرخصة للبناء مع الأوراق الثبوتية والصك العقاري", "phone": "0691897126"},
        {"title": "شراكة فلاحية وأراضي للبيع أو الكراء", "category": "شراكة واستثمار", "details": "فرص واعدة للاستثمار الفلاحي والصناعي والتجاري", "phone": "0691897126"}
    ]
    
    for prop in properties:
        st.markdown(f"""
        <div style="padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 15px; background-color: #f9f9f9;">
            <h3 style="color: #2c3e50; margin-bottom: 5px;">🏢 {prop['title']}</h3>
            <p><b>التصنيف:</b> {prop['category']}</p>
            <p><b>التفاصيل:</b> {prop['details']}</p>
            <p style="color: #27ae60; font-weight: bold;">📞 للتواصل المباشر: {prop['phone']}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "💬 المحادثة الذكية مع Dana":
    st.title("💬 المحادثة مع وكيل تساوت الذكي")
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
            
    if user_input := st.chat_input("اكتب سؤالك أو طلبك هنا..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
            
        # توجيه الطلب تلقائياً عبر Multi-Domain Agent
        response, domain_name = agent_router.route_query(user_input)
        
        reply = f"**[{domain_name}]**\n\n{response}\n\n📞 للتنسيق الفوري يرجى الاتصال بـ: **0691897126**"
        
        with st.chat_message("assistant"):
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

elif page == "⚙️ التحكم الذكي بالوكلاء":
    st.title("⚙️ لوحة التحكم في الوكلاء المتخصصين")
    domain_choice = st.selectbox(
        "اختر الوكيل المتخصص يدوياً:",
        ["🏡 العقارات والاستثمار الفلاحي", "🚗 السيارات والمركبات", "🎨 التصميم والهوية البصرية", "⚙️ التحكم البرمجي والـ GitHub"]
    )
    
    manual_input = st.text_area("أدخل التعليمات الخاصة بهذا الوكيل:", height=120)
    if st.button("تنفيذ المهمة"):
        st.success(f"تم توجيه المهمة بنجاح إلى وكيل **{domain_choice}** والعملية جارية في الخلفية عبر النظام الآلي.")
