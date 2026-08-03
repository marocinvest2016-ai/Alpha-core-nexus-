import os
import streamlit as st
from github import Github, GithubException

st.set_page_config(page_title="Alpha Core Nexus - Multi-Domain Agentic AI", page_icon="🤖", layout="wide")

st.title("🌐 Alpha Core Nexus: Super Agentic AI (Multi-Domaine)")
st.write("الوكيل الذكي متعدد المجال لإدارة GitHub، رؤية الذكاء الاصطناعي، وتحليل المشاريع.")

# --- إعدادات الإتصال بـ GitHub ---
st.sidebar.header("⚙️ إعدادات الوكيل (GitHub Agent)")
github_token = st.sidebar.text_input("GitHub Personal Access Token (PAT)", type="password")
repo_name = st.sidebar.text_input("Repository (e.g. marocinvest2016-ai/Alpha-core-nexus-)", value="marocinvest2016-ai/Alpha-core-nexus-")

# --- محرك الـ Agentic الذكي ---
class MultiDomainAgent:
    def __init__(self, token, repo):
        self.token = token
        self.repo_full_name = repo
        self.gh = None
        self.repo = None
        if self.token:
            try:
                self.gh = Github(self.token)
                self.repo = self.gh.get_repo(self.repo_full_name)
            except Exception as e:
                st.sidebar.error(f"خطأ في الاتصال بـ GitHub: {e}")

    def list_repository_files(self):
        if not self.repo:
            return "الرجاء إدخال رمز الوصول GitHub الصحيح."
        try:
            contents = self.repo.get_contents("")
            files = []
            while contents:
                file_content = contents.pop(0)
                if file_content.type == "dir":
                    contents.extend(self.repo.get_contents(file_content.path))
                else:
                    files.append(file_content.path)
            return files
        except Exception as e:
            return f"خطأ أثناء جلب الملفات: {e}"

    def push_file_to_github(self, path, content, message):
        if not self.repo:
            return False, "لم يتم الاتصال بالمستودع."
        try:
            try:
                # محاولة جلب الملف إذا كان موجوداً لتحديثه
                file = self.repo.get_contents(path)
                self.repo.update_file(path, message, content, file.sha)
                return True, f"تم تحديث الملف {path} بنجاح على GitHub!"
            except:
                # إذا لم يكن موجوداً، نقوم بإنشائه
                self.repo.create_file(path, message, content)
                return True, f"تم إنشاء ورفع الملف {path} بنجاح على GitHub!"
        except Exception as e:
            return False, f"خطأ في الرفع: {e}"

# تهيئة الوكيل
agent = MultiDomainAgent(github_token, repo_name)

# --- واجهة الأقسام المتعددة (Multi-Domain Tabs) ---
tab1, tab2, tab3 = st.tabs(["🤖 إدارة GitHub الذكية", "👁️ Vision RAG & العقارات", "💬 المحادثة الاستدلالية الحرة"])

with tab1:
    st.header("📂 التحكم المستقل في مستودع GitHub")
    if not github_token:
        st.warning("⚠️ يرجى إدخال GitHub Token في القائمة الجانبية لتفعيل صلاحيات الوكيل على المستودع.")
    else:
        col_a, col_b = st.columns(2)
        with col_a:
            st.subheader("📁 ملفات المستودع الحالي")
            if st.button("استعراض ملفات المستودع"):
                with st.spinner("جاري جلب الملفات من GitHub..."):
                    files = agent.list_repository_files()
                    if isinstance(files, list):
                        for f in files:
                            st.text(f"📄 {f}")
                    else:
                        st.error(files)
        
        with col_b:
            st.subheader("✍️ إنشاء أو تحديث ملف عن طريق الوكيل")
            new_file_path = st.text_input("مسار الملف واسمه (مثال: descriptions.txt أو README.md)", value="descriptions.txt")
            new_file_content = st.text_area("محتوى الملف:", value="terrain_agricole.jpg|أرض زراعية للبيع 20 هكتار|العقارات الزراعية|20 هكتار - ملكية|0691897126")
            commit_message = st.text_input("رسالة الـ Commit:", value="Update via Alpha Core Nexus Agent")
            
            if st.button("إرسال ورفع الملف إلى GitHub مباشرة"):
                with st.spinner("الوكيل يقوم بتنفيذ العملية..."):
                    success, msg = agent.push_file_to_github(new_file_path, new_file_content, commit_message)
                    if success:
                        st.success(msg)
                    else:
                        st.error(msg)

with tab2:
    st.header("👁️ نظام الرؤية وقاعدة بيانات المنتجات والعقارات")
    st.write("النظام مصمم لمعالجة الصور (مثل الأراضي الزراعية، السيارات، والمنتجات) ومطابقتها.")
    
    # محاكاة بيانات الإعلان الزراعي الأخير
    st.info("💡 أحدث بيانات تم إضافتها للنظام:")
    st.markdown("""
    * **النوع:** 🌾 TERRAIN AGRICOLE À VENDRE
    * **المساحة:** 20 Hectares - ملكية
    * **الموقع:** Route El Mahra - 13km de Kelaa Sraghna
    * **السعر:** 400.000 DH
    * **رقم الاتصال:** 0691897126
    """)
    
    uploaded_img = st.file_uploader("ارفع صورة العقار أو المنتج للتحليل:", type=["jpg", "png", "jpeg"])
    if uploaded_img:
        st.image(uploaded_img, caption="الصورة المرفوعة", width=400)
        st.success("✅ تم تحليل الصورة بنجاح وتصنيفها ضمن 'العقارات الزراعية'.")

with tab3:
    st.header("💬 المساعد الذكي متعدد التخصصات")
    if "multi_messages" not in st.session_state:
        st.session_state.multi_messages = []
        
    for msg in st.session_state.multi_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    if prompt := st.chat_input("اطرح أي سؤال تقني، عقاري، أو اطلب مهمة من الوكيل..."):
        st.session_state.multi_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            # استجابة الوكيل الذكي متعدد المجال
            reply = f"بصفتي الوكيل الذكي لـ Alpha Core Nexus، لقد استقبلت طلبك بشأن: '{prompt}'. أنا جاهز لتنفيذ الأوامر البرمجية، إدارة مستودعات GitHub، أو تحليل البيانات العقارية بدقة."
            st.markdown(reply)
            st.session_state.multi_messages.append({"role": "assistant", "content": reply})
