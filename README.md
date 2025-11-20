# AI Resume Analyzer  
**Instantly score any resume against a job description using local/open-source LLMs**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Runs offline](https://img.shields.io/badge/Runs-100%25%20offline-green)](#)

## Features

- Upload PDF or DOCX resumes  
- Paste any job description  
- Get a precise **0–100 match score** in seconds  
- Detailed feedback: strengths, missing skills, improvement suggestions  
- Full **ATS compatibility check** (tables, images, fonts, etc.)  
- 100 % local & private — runs completely offline with Ollama + Llama 3.1 (or any model you prefer)  
- One-click swap to OpenAI / Groq / Anthropic for higher accuracy  


## Quick Start (under 2 minutes)

```bash
# 1. Clone the repo
git clone https://github.com/GustavoPrietoP/resume_analyzer.git
cd resume_analyzer

# 2. Install dependencies
pip install streamlit PyPDF2 docx2txt ollama

# 3. Pull a model (Llama 3.1 8B recommended)
ollama pull llama3.1:8b

# 4. Run the app
streamlit run resume_analyzer.py
```

Open http://localhost:8501 and start analyzing!

## Tech Stack

- **Frontend/UI**: Streamlit  
- **Backend & LLM**: Ollama (local) – easily switch to OpenAI/Groq/Anthropic  
- **Document Parsing**: PyPDF2 + docx2txt  
- **Model used locally**: Meta Llama 3.1 8B (or Mistral, Gemma 2, Phi-3, etc.)  

## Deploy for Free (optional)

1. Push this repo to GitHub  
2. Go to https://share.streamlit.io  
3. Connect your repo → deploy in 30 seconds  
4. Share the public link on your resume/portfolio  

## License

MIT © Gustavo Prieto – feel free to fork and star :)
