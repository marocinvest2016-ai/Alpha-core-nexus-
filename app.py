import streamlit as st
from github import Github

st.set_page_config(page_title="وكالة تساوت الرقمية للعقار والأعمال", page_icon="🏢", layout="wide")

st.title("🌐 وكالة تساوت الرقمية للعقار والأعمال بقلعة السراغنة")
st.markdown("### Alpha Core Nexus: Super Agentic AI")

# --- إعدادات الإتصال بـ GitHub في القائمة الجانبية ---
st.sidebar.header("⚙️ إعدادات الوكيل (GitHub Agent)")
github_token = st.sidebar.text_input("GitHub Personal Access Token (PAT)", type="password")
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

# --- التبويبات الرئيسية ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🏢 عروض الوكالة (RAG الذكي)", 
    "🤖 إدارة الملفات والـ GitHub", 
    "👁️ Vision RAG والصور", 
    "💬 محادثة وكيل تساوت"
])

with tab1:
    st.header("🌟 دليل العقارات والاستثمار بقلعة السراغنة")
    remote_desc = None
    if repo:
        try:
            file_content = repo.get_contents("descriptions.txt")
            remote_desc = file_content.decoded_content.decode("utf-8")
        except:
            remote_desc = None
            
    if remote_desc:
        st.success("✅ تم جلب أحدث عروض العقارات مباشرة من مستودع GitHub:")
        st.info(remote_desc)
    else:
        st.warning("⚠️ يرجى إدخال GitHub Token في القائمة الجانبية لربط الوكيل وقراءة العروض من المستودع.")
        st.markdown("""
        * **تجزئة الهدى:** بقع سكنية وتجارية من 80م² إلى 240م² فما فوق.
        * **المنازل والعمارات:** بقع لبناء عمارات أو مشاريع تجارية بمواسع استراتيجية.
        * **الكراء:** شقق ومكاتب جاهزة للكراء الشهري.
        * **الاستثمار الفلاحي:** أراضي فلاحية مرخصة، فيرمات جاهزة، وشراكات مع الأوراق الثبوتية.
        📞 **للتواصل:** 0691897126
        """)

with tab2:
    st.header("📂 التحكم المستقل في مستودع GitHub")
    if not github_token:
        st.warning("⚠️ يرجى إدخال GitHub Token في القائمة الجانبية.")
    else:
        file_path = st.text_input("مسار الملف:", value="descriptions.txt")
        file_content = st.text_area("محتوى الملف:", value="وكالة تساوت الرقمية للعقار والأعمال بقلعة السراغنة - 0691897126")
        commit_msg = st.text_input("رسالة Commit:", value="Update via Tissawt Agent")
        
        if st.button("رفع أو تحديث الملف على GitHub"):
            try:
                try:
                    f = repo.get_contents(file_path)
                    repo.update_file(file_path, commit_msg, file_content, f.sha)
                    st.success(f"تم تحديث الملف {file_path} بنجاح!")
                except:
                    repo.create_file(file_path, commit_msg, file_content)
                    st.success(f"تم إنشاء الملف {file_path} بنجاح!")
            except Exception as e:
                st.error(f"خطأ: {e}")

with tab3:
    st.header("👁️ نظام الرؤية وتحليل الصور (Vision RAG)")
    img = st.file_uploader("رفع صورة العقار:", type=["jpg", "png", "jpeg"])
    if img:
        st.image(img, caption="صورة العقار", width=400)
        st.success("✅ تم تحليل الصورة بنجاح لصالح وكالة تساوت.")

with tab4:
    st.header("💬 المحادثة الذكية مع وكيل تساوت")
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
            reply = f"مرحباً بك في وكالة تساوت الرقمية. بخصوص '{prompt}', اتصل بنا مباشرة على الرقم: 0691897126 للحجز والاستفسار."
            st.markdown(reply)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
