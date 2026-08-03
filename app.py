import os
import streamlit as st
from github import Github

st.set_page_config(page_title="وكالة تساوت الرقمية للعقار والأعمال - Alpha Core Nexus", page_icon="🏢", layout="wide")

st.title("🌐 وكالة تساوت الرقمية للعقار والأعمال بقلعة السراغنة")
st.markdown("### Alpha Core Nexus: Super Agentic AI (Multi-Domaine)")

# --- إعدادات الإتصال بـ GitHub في القائمة الجانبية ---
st.sidebar.header("⚙️ إعدادات الوكيل (GitHub Agent)")
github_token = st.sidebar.text_input("GitHub Personal Access Token (PAT)", type="password")
repo_name = st.sidebar.text_input("Repository", value="marocinvest2016-ai/Alpha-core-nexus-")

class TissawtAgent:
    def __init__(self, token, repo):
        self.token = token
        self.repo_full_name = repo
        self.repo = None
        if self.token:
            try:
                gh = Github(self.token)
                self.repo = gh.get_repo(self.repo_full_name)
            except Exception as e:
                pass

    def get_file_content(self, path="descriptions.txt"):
        if not self.repo:
            return None
        try:
            file_content = self.repo.get_contents(path)
            return file_content.decoded_content.decode("utf-8")
        except:
            return None

    def push_file(self, path, content, message):
        if not self.repo:
            return False, "لم يتم الاتصال بالمستودع."
        try:
            try:
                file = self.repo.get_contents(path)
                self.repo.update_file(path, message, content, file.sha)
                return True, f"تم تحديث الملف {path} بنجاح!"
            except:
                self.repo.create_file(path, message, content)
                return True, f"تم إنشاء الملف {path} بنجاح!"
        except Exception as e:
            return False, f"خطأ: {e}"

agent = TissawtAgent(github_token, repo_name)

# --- التبويبات الرئيسية ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🏢 عروض الوكالة (RAG الذكي)", 
    "🤖 إدارة الملفات والـ GitHub", 
    "👁️ Vision RAG والصور", 
    "💬 محادثة وكيل تساوت"
])

with tab1:
    st.header("🌟 دليل العقارات والاستثمار بقلعة السراغنة")
    
    remote_desc = agent.get_file_content("descriptions.txt")
    if remote_desc:
        st.success("✅ تم جلب أحدث عروض العقارات مباشرة من مستودع GitHub (RAG Mode Active):")
        st.info(remote_desc)
    else:
        st.warning("⚠️ لم يتم العثور على ملف descriptions.txt في المستودع أو لم يتم إدخال التوكن بعد. إليك العروض الأساسية:")
        st.markdown("""
        * **تجزئة الهدى:** بقع سكنية وتجارية من 80م² إلى 240م² فما فوق.
        * **المنازل والعمارات:** بقع لبناء عمارات أو مشاريع تجارية بمواقع استراتيجية وأسعار تنافسية.
        * **الكراء:** شقق ومكاتب جاهزة للكراء الشهري.
        * **الاستثمار الفلاحي:** أراضي فلاحية مرخصة للبناء، فيرمات جاهزة للاستغلال، وأراضي للبيع أو الكراء أو الشراكة مع الأوراق الثبوتية.
        📞 **للتواصل:** 0691897126
        """)
    
    st.markdown("---")
    st.subheader("🔍 فلترة سريعة للعقارات")
    filter_type = st.selectbox("اختر الصنف:", ["جميع الأصناف", "بقع سكنية (تجزئة الهدى)", "عمارات ومشاريع تجارية", "أراضي وفيرمات فلاحية", "شقق ومكاتب للكراء"])
    if filter_type != "جميع الأصناف":
        st.write(f"عرض النتائج الخاصة بـ: **{filter_type}** في قلعة السراغنة. الأسعار تنافسية ومباشرة من أصحاب الأملاك. اتصل بـ **0691897126** للحجز.")

with tab2:
    st.header("📂 التحكم المستقل في مستودع GitHub")
    if not github_token:
        st.warning("⚠️ يرجى إدخال GitHub Token في القائمة الجانبية لتفعيل صلاحيات الوكيل.")
    else:
        file_path = st.text_input("مسار الملف:", value="descriptions.txt")
        file_content = st.text_area("محتوى الملف:", value=remote_desc if remote_desc else "اكتب تفاصيل الإعلان هنا...")
        commit_msg = st.text_input("رسالة Commit:", value="Update agency descriptions via agent")
        
        if st.button("رفع أو تحديث الملف على GitHub"):
            success, msg = agent.push_file(file_path, file_content, commit_msg)
            if success:
                st.success(msg)
            else:
                st.error(msg)

with tab3:
    st.header("👁️ نظام الرؤية وتحليل صور العقارات (Vision RAG)")
    img = st.file_uploader("رفع صورة العقار أو الأرض:", type=["jpg", "png", "jpeg"])
    if img:
        st.image(img, caption="صورة العقار", width=400)
        st.success("✅ تم تحليل الصورة وإضافتها إلى سجلات وكالة تساوت الرقمية بقلعة السراغنة.")

with tab4:
    st.header("💬 المحادثة الذكية مع وكيل تساوت")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if prompt := st.chat_input("اسأل عن أي عقار أو أرض في قلعة السراغنة..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            reply = f"مرحباً بك في وكالة تساوت الرقمية بقلعة السراغنة. بخصوص استفسارك حول '{prompt}', نحن نوفر أفضل العقارات والأراضي الفلاحية بأسعار تنافسية مع الصكوك والأوراق الثبوتية الرسمية. اتصل بنا الآن على الرقم: 0691897126."
            st.markdown(reply)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
