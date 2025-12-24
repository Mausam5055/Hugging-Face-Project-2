import os
import torch
import numpy as np
from bark import generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

# Hack to fix PyTorch > 2.6 default weights_only=True breaking Bark
# We need to allow numpy scalars or revert to unsafe load for the session
try:
    # Option 1: Add safe globals if supported
    if hasattr(torch.serialization, "add_safe_globals"):
        # We need to get the actual class object for numpy.core.multiarray.scalar
        # In newer numpy this might be different, but let's try to find it or workaround
        # The error specifically mentions 'numpy.core.multiarray.scalar'
        from numpy.core.multiarray import scalar
        torch.serialization.add_safe_globals([scalar])
except ImportError:
    # Fallback: specific numpy version might not expose it there
    pass
except Exception as e:
    print(f"Warning: Could not add safe globals: {e}")

# Option 2: Monkeypatch torch.load to default weights_only=False if not specified
# This is necessary because we cannot easily change the calls inside the 'bark' library
_original_load = torch.load

def safe_load(*args, **kwargs):
    if "weights_only" not in kwargs:
        kwargs["weights_only"] = False
    return _original_load(*args, **kwargs)

torch.load = safe_load

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
