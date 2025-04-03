import streamlit as st
from similarity import calculate_similarity
import PyPDF2
import docx
import os

# Page config
st.set_page_config(
    page_title="Plagiarism Checker",
    page_icon="🔍",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stProgress > div > div > div > div {
        background-color: #FF4B4B;
    }
    .st-b7 {
        color: #FF4B4B;
    }
</style>
""", unsafe_allow_html=True)

# Helper functions for file handling
def extract_text_from_file(file):
    """Extract text from .txt, .pdf, or .docx files"""
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() for page in pdf_reader.pages])
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])
    else:
        return None

# Main UI
st.title("🔍 Basic Plagiarism Checker")
st.caption("Compare text or documents using TF-IDF and cosine similarity")

# Input options
tab1, tab2 = st.tabs(["Text Input", "File Upload"])

with tab1:
    text1 = st.text_area("Enter first text:", height=150)
    text2 = st.text_area("Enter second text:", height=150)
    text_btn = st.button("Check Similarity (Text)")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        file1 = st.file_uploader("Upload first file:",
                                 type=["txt", "pdf", "docx"])
    with col2:
        file2 = st.file_uploader("Upload second file:",
                                 type=["txt", "pdf", "docx"])
    file_btn = st.button("Check Similarity (Files)")

# Process inputs
if text_btn and text1 and text2:
    with st.spinner("Calculating..."):
        similarity = calculate_similarity(text1, text2)
        st.success(f"Similarity: {similarity}%")
        # Visual indicator
        st.progress(similarity/100)
        if similarity > 70:
            st.error("⚠️ High similarity detected (potential plagiarism)")
        elif similarity > 30:
            st.warning("Moderate similarity detected")
        else:
            st.success("Low similarity detected")

elif file_btn and file1 and file2:
    with st.spinner("Processing files..."):
        text1 = extract_text_from_file(file1)
        text2 = extract_text_from_file(file2)
        if text1 and text2:
            similarity = calculate_similarity(text1, text2)
            st.success(f"Similarity between {file1.name} and {file2.name}: {similarity}%")
            st.progress(similarity/100)
            if similarity > 70:
                st.error("⚠️ High similarity detected (potential plagiarism)")
            elif similarity > 30:
                st.warning("Moderate similarity detected")
            else:
                st.success("Low similarity detected")
        else:
            st.error("Could not extract text from files")

# Footer
st.markdown("---")
st.caption("Project by [Your Name] | Uses TF-IDF and cosine similarity")