import gradio as gr
from tts.bark_tts import BarkTTS
import numpy as np

# Initialize TTS engine once
# Using small models by default to avoid OOM on standard CPUs
tts = BarkTTS(use_small_models=True)

def text_to_speech(text):
    if not text.strip():
        raise gr.Error("Please enter some text.")
    
    print(f"Processing: {text}")
    try:
        # Generate audio
        sample_rate, audio_array = tts.generate(text)
        return (sample_rate, audio_array)
    except Exception as e:
        print(f"Error: {e}")
        raise gr.Error(f"Generation failed: {str(e)}")

# Custom CSS for better look
custom_css = """
footer {visibility: hidden}
"""

with gr.Blocks(title="Universal Multilingual TTS", css=custom_css, theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 🌍 Universal Multilingual Text-to-Speech (Offline)
    
    Generate natural-sounding speech from text in various languages using **Suno Bark**.
    This runs entirely locally on your machine.
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            text_input = gr.Textbox(
                label="Input Text", 
                placeholder="Type anything in English, Hindi, Spanish, French, etc...", 
                lines=5
            )
            generate_btn = gr.Button("📢 Generate Speech", variant="primary", size="lg")
            
            gr.Markdown("""
            ### Instructions
            1. Enter text in **any supported language**.
            2. Click **Generate Speech**.
            3. Wait for the model to generate (first run may take longer).
            """)
        
        with gr.Column(scale=1):
            audio_output = gr.Audio(label="Generated Audio", type="numpy", interactive=False)
            
    generate_btn.click(
        fn=text_to_speech, 
        inputs=text_input, 
        outputs=audio_output,
        concurrency_limit=1
    )

if __name__ == "__main__":
    # Launch locally
    app.launch(server_name="127.0.0.1", server_port=7860, inbrowser=True)
