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
```

### 2. Install Required Libraries
Install the necessary Python packages:
```bash
# Install Coqui TTS and Gradio interface
pip install coqui-tts
pip install gradio
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
python main.py
```

## Next Steps
After installation, you can start experimenting with different TTS models and configurations available through the Coqui TTS library.