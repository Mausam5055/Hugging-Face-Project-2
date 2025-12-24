import soundfile as sf
import numpy as np
import os

def save_audio(file_path: str, sample_rate: int, audio_data: np.ndarray):
    """
    Saves the numpy audio array to a WAV file.
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    sf.write(file_path, audio_data, sample_rate)
    print(f"Audio saved to {file_path}")
