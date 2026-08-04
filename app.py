import streamlit as st
from github import Github

st.set_page_config(page_title="وكالة تساوت الرقمية للعقار والأعمال", page_icon="🏢", layout="wide")

# --- القائمة الجانبية المنسدلة للتنقل ---
st.sidebar.title("🏢 وكالة تساوت الرقمية")
page = st.sidebar.selectbox("اختر الخدمة", ["🏠 الرئيسية", "📋 عرض العقارات", "💬 المحادثة الذكية مع وكيل تساوت", "🤖 إدارة الملفات والـ GitHub", "📞 اتصل بنا"])

# إعدادات الإتصال بـ GitHub في القائمة الجانبية
st.sidebar.markdown("---")
st.sidebar.header("⚙️ إعدادات الوكيل (GitHub)")
github_token = st.sidebar.text_input("GitHub Token", type="password")
repo_name = st.sidebar.text_input("Repository", value="marocinvest2016-ai/Alpha-core-nexus-")

def get_agent_repo(token, repo_fullName):
    if not token:
        return None
    try:
        gh = Github(token)
        return gh.get_repo(repo_fullName)
    except:
        return None

repo = get_agent_repo(github_token, repo_name)

# --- الصفحة الرئيسية ---
if page == "🏠 الرئيسية":
    st.title("🌐 وكالة تساوت الرقمية للعقار والأعمال")
    st.subheader("قلعة السراغنة - في خدمتكم")
    st.markdown("""
    مرحباً بك في المنصة الرقمية الرسمية لوكالة تساوت. نحن نقدم خدمات عقارية متكاملة، استثمارات فلاحية، وشقق ومكاتب للكراء بقلعة السراغنة ومحيطها.
    """)
    st.info("استخدم القائمة الجانبية لتصفح العروض، التحدث مع الوكيل الذكي، أو إدارة المحتوى.")

# --- عرض العقارات بتصميم بطاقات أنيقة ---
elif page == "📋 عرض العقارات":
    st.title("📋 جميع العروض العقارية والاستثمارية")
    
    remote_desc = None
    if repo:
        try:
            file_content = repo.get_contents("descriptions.txt")
            remote_desc = file_content.decoded_content.decode("utf-8")
        except:
            remote_desc = None
            
    if remote_desc:
        st.success("✅ تم جلب أحدث العروض مباشرة من مستودع GitHub:")
        
        # عرض البيانات المنسقة ببطاقات
        lines = remote_desc.split("\n")
        for line in lines:
            if line.strip():
                parts = line.split("|")
                if len(parts) >= 5:
                    img_name, title, category, details, phone = parts[0], parts[1], parts[2], parts[3], parts[4]
                    
                    with st.container():
                        st.markdown(f"""
                        <div style="padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; margin-bottom: 15px; background-color: #f9f9f9;">
                            <h3 style="color: #2c3e50; margin-bottom: 5px;">🏢 {title}</h3>
                            <p><b>التصنيف:</b> {category}</p>
                            <p><b>التفاصيل:</b> {details}</p>
                            <p style="color: #27ae60; font-weight: bold;">📞 للتواصل: {phone}</p>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    # سطر احتياطي في حال كان النص عادي غير مقسم
                    st.info(line)
    else:
        st.warning("⚠️ يرجى إدخال GitHub Token في القائمة الجانبية لربط الوكيل وقراءة العروض المحدثة.")

# --- المحادثة الذكية ---
elif page == "💬 المحادثة الذكية مع وكيل تساوت":
    st.title("💬 المحادثة الذكية مع وكيل تساوت")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    for m in st.session_state.chat_history:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
    if prompt := st.chat_input("اسأل عن عقارات قلعة السراغنة..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            reply = f"مرحباً بك في وكالة تساوت الرقمية بقلعة السراغنة. بخصوص طلبك '{prompt}', يرجى الاتصال بنا مباشرة على الرقم: 0691897126 للحجز والاستفسار الفوري."
            st.markdown(reply)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})

# --- إدارة الملفات والـ GitHub ---
elif page == "🤖 إدارة الملفات والـ GitHub":
    st.title("🤖 التحكم المستقل في مستودع GitHub")
    if not github_token:
        st.warning("⚠️ يرجى إدخال GitHub Token في القائمة الجانبية لتفعيل خاصية التعديل.")
    else:
        file_path = st.text_input("مسار الملف:", value="descriptions.txt")
        file_content = st.text_area("محتوى الملف الجديد:", value="tazette_terrain.jpg|بقع سكنية وتجارية للبيع في تجزئة الهدى|بقع سكنية وتجارية|من 80م² إلى 240م² مع موقع استراتيجي وأسعار تنافسية|0691897126")
        commit_msg = st.text_input("رسالة الـ Commit:", value="Update descriptions.txt via Agent")
        
        if st.button("رفع وتحديث الملف على GitHub"):
            try:
                try:
                    f = repo.get_contents(file_path)
                    repo.update_file(file_path, commit_msg, file_content, f.sha)
                    st.success(f"تم تحديث الملف {file_path} بنجاح!")
                except:
                    repo.create_file(file_path, commit_msg, file_content)
                    st.success(f"تم إنشاء الملف {file_path} بنجاح!")
            except Exception as e:
                st.error(f"خطأ أثناء الرفع: {e}")

# --- اتصل بنا ---
elif page == "📞 اتصل بنا":
    st.title("📞 اتصل بوكالة تساوت الرقمية")
    st.markdown("""
    * **المدينة:** قلعة السراغنة، المغرب.
    * **الهاتف الرسمي للتواصل:** 0691897126
    * **الخدمات:** العقارات السكنية والتجارية، الاستثمار الفلاحي، والتجارة والخدمات الرقمية.
    """)
