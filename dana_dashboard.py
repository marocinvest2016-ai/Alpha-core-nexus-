import streamlit as st
import datetime
import os

st.set_page_config(page_title="DANA CONTROL PANEL", layout="wide")

st.title("🤖 DANA CONTROL PANEL v1.0")
st.success("Dana is ONLINE and managing: marocinvest2016-ai/Alpha-core-nexus-")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Status", "ONLINE", "Active")
with col2:
    st.metric("Mode", "Full Auto")
with col3:
    st.metric("Last Update", datetime.datetime.now().strftime("%H:%M:%S"))

st.divider()

st.header("📦 Current Product")
if os.path.exists("PRODUCT.md"):
    with open("PRODUCT.md", "r") as f:
        st.code(f.read(), language="markdown")

st.header("📜 System Logs")
if os.path.exists("DANA_REPORT.md"):
    with open("DANA_REPORT.md", "r") as f:
        st.code(f.read(), language="markdown")

st.caption("Managed by DANA-AGENT | TDL-2026")
