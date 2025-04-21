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

# Initialize TTS with a single language model
# Using the Indonesian model as in your original code
tts = TTS("tts_models/ind/fairseq/vits").to(device)

# Function to generate audio from text
def generate_audio(text):
    if not text.strip():
        return None, "Please enter some text to convert to speech."
    
    try:
        output_path = f"outputs/output_idn_{int(time.time())}.wav"
        # For single language model, we don't need to specify language
        tts.tts_to_file(
            text=text,
            file_path=output_path
        )
        return output_path, "✅ Audio generated successfully!"
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

with gr.Blocks(title="Advanced Text-to-Speech Generator", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🎙️ Text-to-Speech Generator
        
        Transform your text into natural-sounding speech using Indonesian TTS model.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=2):
            text_input = gr.Textbox(
                label="Text to Convert",
                placeholder="Enter the text you want to convert to speech...",
                lines=6
            )
            
            generate_button = gr.Button("🔊 Generate Speech", variant="primary")
            status = gr.Markdown("Ready to generate audio")
        
        with gr.Column(scale=1):
            audio_output = gr.Audio(label="Generated Audio")
            with gr.Accordion("System Info", open=False):
                gr.Markdown(f"""
                - **Device**: {device}
                - **Model**: Indonesian TTS (fairseq/vits)
                - **Voices Available**: {len(tts.speakers) if tts.speakers else 0}
                """)
    
    # Handle button click - simplified to remove language parameter
    generate_button.click(
        fn=generate_audio,
        inputs=[text_input],
        outputs=[audio_output, status]
    )

demo.launch()