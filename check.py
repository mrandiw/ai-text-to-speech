import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU device name: {torch.cuda.get_device_name(0)}")

from TTS.utils.manage import ModelManager

# Get the TTS model manager
manager = ModelManager()

# Print the model download directory
print(f"TTS models are cached at: {manager.output_prefix}")

import os
from pathlib import Path

# Check common TTS model locations
locations = [
    os.path.expanduser("~/.local/share/tts"),
    os.path.expanduser("~/AppData/Local/tts"),
    os.path.join(os.getenv("LOCALAPPDATA", ""), "tts"),
    os.path.join(os.getenv("APPDATA", ""), "tts")
]

for loc in locations:
    path = Path(loc)
    if path.exists():
        print(f"Found TTS directory: {path}")
        # List contents
        for item in path.iterdir():
            print(f" - {item}")