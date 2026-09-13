# AI-Assisted Authorship Detection & Google Docs Analyzer

An AI-assisted authorship analysis tool that analyzes Google Docs content and revision metadata. It uses a local Hugging Face NLP model to identify AI-like writing patterns and combines them with document editing behavior.

## Features

- Google Docs & Drive API integration
- OAuth 2.0 authentication
- Document text extraction
- Revision analysis
- Editing-burst detection
- Local Hugging Face AI detection
- AI-likelihood scoring
- Automated analysis reports

## Tech Stack

- Python
- FastAPI
- Google Docs API
- Google Drive API
- Hugging Face Transformers
- PyTorch
- RoBERTa

## Setup

```bash
git clone https://github.com/MirzaMirzazada/AI-Detection-Google-Docs
cd AI-Detection-Google-Docs

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt