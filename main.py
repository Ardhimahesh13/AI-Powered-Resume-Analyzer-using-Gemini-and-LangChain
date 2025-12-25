import streamlit as st
import pandas as pd
import os
import zipfile
from typing import TypedDict
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from docx import Document
from langchain_google_genai import ChatGoogleGenerativeAI

# Setting the environment
load_dotenv()

# Define the Schema 
class Resumeschema(TypedDict):
    full_name: str
    email: str
    skills: list[str]
    github_links: str
    summary: str

# Text extraction function 
def extracted_text(file):
    text = ""
    
    if file.name.endswith(".pdf"):
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    elif file.name.endswith('.docx'): 
        doc = Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    return text 

def main():
    st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
    st.title("📄 AI-Powered Resume Analyzer")
    st.write("Upload a ZIP file containing resumes (PDF/DOCX) to extract details into a CSV.") 

    # Initialize the Gemini LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    structured_llm = llm.with_structured_output(Resumeschema)

    # Upload File
    uploader_zip = st.file_uploader("Upload ZIP folder", type=["zip"])
    
    if uploader_zip:
        results = []

        # Open the zip file 
        with zipfile.ZipFile(uploader_zip, 'r') as z:
            resume_files = [f for f in z.namelist() if f.endswith(('.pdf', '.docx'))]
            
            if not resume_files:
                st.error("No PDF or DOCX files found in the zip")
                return
            
            st.info(f"Processing {len(resume_files)} resumes...")
            progress_bar = st.progress(0)

            
            for i, file_name in enumerate(resume_files):
                with z.open(file_name) as f:
                    # Extract raw text
                    raw_text = extracted_text(f)

                    # Extract structured data 
                    response = structured_llm.invoke(f"Extract key details from this resume text:\n\n{raw_text}")
                    results.append(response)
                
                progress_bar.progress((i + 1) / len(resume_files))

        # Create CSV and Display 
        if results:
            df = pd.DataFrame(results)
            st.success("Extraction Complete!")
            st.dataframe(df)

            # Download CSV button 
            csv_data = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download extracted data as CSV",
                data=csv_data,
                file_name="resume_analysis.csv",
                mime="text/csv"
            )

if __name__ == "__main__":
    main()