# streamlit_app.py
import streamlit as st
import requests

st.set_page_config(page_title="AAA Complaint Generator", layout="wide")
st.title("📝 Florida Arbitration Complaint Generator")

user_facts = st.text_area("Enter factual background", height=300)

if st.button("Generate Complaint"):
    with st.spinner("Generating complaint..."):
        response = requests.post("http://localhost:8000/generate-rag-case/", json={"user_facts": user_facts})
        if response.status_code == 200:
            result = response.json()
            st.success("✅ Complaint generated!")

            st.subheader("📄 PDF Output")
            st.markdown(f"[Download PDF]({result['pdf_path']})", unsafe_allow_html=True)

            st.subheader("📋 Section Preview")
            for i, section in enumerate(result["Final"]):
                st.markdown(f"**Section {i+1}:**", unsafe_allow_html=True)
                st.markdown(section, unsafe_allow_html=True)
        else:
            st.error("❌ Failed to generate complaint.")
