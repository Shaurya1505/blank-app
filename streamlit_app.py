import streamlit as st
import pandas as pd
import PyPDF2
import io

st.title("Multi-file Uploader & Content Viewer")

uploaded_files = st.file_uploader(
    "Upload one or more files",
    type=['txt', 'csv', 'pdf'],
    accept_multiple_files=True
)

def display_file_content(file):
    filename = file.name
    st.subheader(f"File: {filename}")

    if filename.endswith('.txt'):
        # Read and display text file
        content = file.read().decode('utf-8')
        st.text(content)
    elif filename.endswith('.csv'):
        # Read and display CSV
        df = pd.read_csv(file)
        st.dataframe(df)
    elif filename.endswith('.pdf'):
        # Read and display PDF content
        reader = PyPDF2.PdfReader(file)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()
        st.text(pdf_text)
    else:
        st.warning("Unsupported file type.")

if uploaded_files:
    for file in uploaded_files:
        display_file_content(file)
else:
    st.info("Please upload one or more files.")

