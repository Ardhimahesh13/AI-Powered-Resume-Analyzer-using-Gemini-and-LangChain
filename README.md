# AI-Powered-Resume-Analyzer-using-Gemini-and-LangChain
AI-Powered Resume Analyzer An automated pipeline to process bulk resumes from ZIP files using LangChain and Google Gemini. Extract structured data (skills, summary, links) from PDF/DOCX formats into a downloadable CSV. Built with Streamlit for a seamless HR workflow—eliminating manual data entry and inconsistency

# Project Overview

HR teams and recruiters frequently struggle to analyze large volumes of resumes efficiently because resume formats vary widely (PDF, DOCX, different layouts, fonts, and structures). Manually reviewing each resume and extracting candidate information is time-consuming, error-prone, and inconsistent.

This project solves that problem by providing an automated resume-processing pipeline using LangChain and Google Gemini. It converts unstructured resume text into structured data and processes resumes in bulk from a ZIP file, finally exporting all extracted information into a single downloadable CSV file for easy filtering and analysis.

# Key Features

Bulk ZIP Processing
Accepts a ZIP folder containing multiple resumes in PDF or DOCX format.

Automated Information Extraction
Reads each resume and extracts key details using Google Gemini.

Structured Output Enforcement
Uses a TypedDict parser to enforce a fixed schema and maintain data consistency.

CSV Generation
Aggregates extracted details (Name, Email, Skills, Summary, etc.) into a single CSV file.

Web Interface
A simple Streamlit application allows users to upload resumes and download results directly.

# Technical Stack

LLM: Google Gemini 2.5 Flash Lite

Framework: LangChain (Core + Google GenAI)

Frontend: Streamlit

File Parsers:

PyPDF2 (PDF files)

python-docx (DOCX files)

Environment: Python 3.x, VS Code

# Setup and Installation
1. Configure Your Environment

Create a .env file in the project root and add your Google API key:

# 2. Install Dependencies

Create a req.txt file and install dependencies using:pip install -r req.txt

#  Contents of req.txt:
streamlit
pandas
python-dotenv
langchain-google-genai
langchain-core
PyPDF2
python-docx

#  How to Use

Launch the App
Run the following command in your VS Code terminal:
streamlit run app.py

Upload Resumes
Upload a ZIP folder containing multiple PDF or DOCX resumes.

Analyze
The system processes each resume and displays the extracted data in a table.

Export
Click the Download button to save the extracted information as a CSV file.

#  Solution Architecture

The system follows a clean four-step pipeline:

Read
Ingests resumes from the uploaded ZIP file.

Convert
Transforms unstructured resume text into structured data objects using Gemini.

Enforce
Applies TypedDict to maintain a strict and consistent data schema.

Aggregate
Collects all extracted data into a final CSV output.

