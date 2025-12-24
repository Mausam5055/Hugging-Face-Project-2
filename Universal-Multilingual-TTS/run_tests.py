from tts.bark_tts import BarkTTS
from utils.audio_utils import save_audio
import os

if __name__ == "__main__":
    # Use small models for testing to ensure it runs
    tts = BarkTTS(use_small_models=True)
    
    texts = {
        "english": "Hello, this is a test of the Universal Multilingual Text-to-Speech system.",
        "hindi": "नमस्ते, मैं एक बहुभाषी टेक्स्ट-टू-स्पीच सिस्टम हूँ।",
        "spanish": "Hola, este es un sistema de texto a voz multilingüe."
    }

    os.makedirs("output", exist_ok=True)

    for lang, text in texts.items():
        print(f"\n--- Generating for {lang} ---")
        try:
            sample_rate, audio_array = tts.generate(text)
            save_audio(f"output/{lang}.wav", sample_rate, audio_array)
            print(f"Success: Saved output/{lang}.wav")
        except Exception as e:
            print(f"Error generating {lang}: {e}")
