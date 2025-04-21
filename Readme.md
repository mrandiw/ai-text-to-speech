![PythonAnywhere](https://img.shields.io/badge/pythonanywhere-%232F9FD7.svg?style=for-the-badge&logo=pythonanywhere&logoColor=151515)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


# Python With Coqui TTS Implementation

This repository contains setup instructions for working with Coqui TTS, a deep learning toolkit for Text-to-Speech synthesis.

## Repository Reference
- **GitHub**: [https://github.com/idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS)
- **Compatible with**: Python 3.12

## Prerequisites
- Python 3.12 installed on your system
- Git for cloning the repository

## Setup Instructions

### 1. Environment Preparation
Create and activate a Python virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate

# Ubuntu
python -m venv venv
source venv/bin/activate
```

### 2. Install Required Libraries
Install the necessary Python packages:
```bash
# Install Coqui TTS and Gradio interface
pip install coqui-tts
pip install gradio
# for NVIDIA GPU
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 
```

### 3. Verify Installation
Check available TTS models:
```bash
# List all available TTS models
tts --list_models
```

### 4. Run
Check available TTS models:
```bash
# for multy model
python main.py

# for single model
python main_single.py
```

## Next Steps
After installation, you can start experimenting with different TTS models and configurations available through the Coqui TTS library.

## Downloaded Model Located in 
```bash
C:\Users\User\AppData\Local\tts
```