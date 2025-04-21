import torch
import gradio as gr
import os
from TTS.api import TTS
import time

# Create outputs directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Initialize TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
# tts = TTS("tts_models/en/ljspeech/tacotron2-DDC").to(device)

# Function to generate audio from text
def generate_audio(text, speaker, language):
    if not text.strip():
        return None, "Please enter some text to convert to speech."
    
    try:
        output_path = f"outputs/output_{int(time.time())}.wav"
        tts.tts_to_file(
            text=text,
            speaker=speaker,
            language=language,
            file_path=output_path
        )
        return output_path, "✅ Audio generated successfully!"
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

# Available languages
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Polish": "pl",
    "Turkish": "tr",
    "Russian": "ru",
    "Dutch": "nl",
    "Czech": "cs",
    "Arabic": "ar",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi"
}

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎙️ Advanced Text-to-Speech Generator
        
        Transform your text into natural-sounding speech using XTTS v2 technology.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Text to Convert",
                placeholder="Enter the text you want to convert to speech...",
                lines=6
            )
            
            with gr.Row():
                with gr.Column(scale=1):
                    speaker_input = gr.Dropdown(
                        choices=tts.speakers,
                        value=tts.speakers[0],
                        label="Select Voice"
                    )
                
                with gr.Column(scale=1):
                    language_input = gr.Dropdown(
                        choices=list(languages.keys()),
                        value="English",
                        label="Select Language"
                    )
            
            generate_button = gr.Button("🔊 Generate Speech", variant="primary")
            status = gr.Markdown("Ready to generate audio")
        
        with gr.Column(scale=1):
            audio_output = gr.Audio(label="Generated Audio")
            with gr.Accordion("System Info", open=False):
                gr.Markdown(f"""
                - **Device**: {device}
                - **Model**: XTTS v2 (Multilingual)
                - **Voices Available**: {len(tts.speakers)}
                - **Languages**: {len(languages)}
                """)
    
    # Handle button click
    def process_generation(text, speaker, language_name):
        language_code = languages[language_name]
        return generate_audio(text, speaker, language_code)
    
    generate_button.click(
        fn=process_generation,
        inputs=[text_input, speaker_input, language_input],
        outputs=[audio_output, status]
    )

demo.launch()