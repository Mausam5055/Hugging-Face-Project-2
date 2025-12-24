import os
import numpy as np
from bark import generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

class BarkTTS:
    def __init__(self, use_small_models=False):
        self.models_loaded = False
        self.use_small_models = use_small_models
        if use_small_models:
             os.environ["SUNO_USE_SMALL_MODELS"] = "True"

    def load_models(self):
        """
        Preloads the Bark models. 
        This will download models on first run.
        """
        if not self.models_loaded:
            print(f"Loading Bark models (Small={self.use_small_models})... This may take a while on first run.")
            try:
                preload_models(
                    text_use_small=self.use_small_models,
                    coarse_use_small=self.use_small_models,
                    fine_use_small=self.use_small_models
                )
                self.models_loaded = True
                print("Bark models loaded successfully.")
            except Exception as e:
                print(f"Failed to load models: {e}")
                raise e

    def generate(self, text: str):
        """
        Generates audio from text.
        Bark automatically handles multilingual input.
        Returns:
            sample_rate (int): The sample rate of the audio (24000 for Bark).
            audio_array (np.ndarray): The generated audio data.
        """
        if not self.models_loaded:
            self.load_models()
        
        print(f"Generating audio for text: {text[:50]}...")
        # Bark automatically handles language detection based on the text content
        # generic_history_prompt=None lets Bark decide the voice/language
        audio_array = generate_audio(text)
        
        # Bark output is at 24000 Hz
        return 24000, audio_array
