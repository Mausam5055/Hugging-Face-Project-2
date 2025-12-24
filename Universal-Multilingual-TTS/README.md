# Universal Multilingual Text-to-Speech (Offline)

> **Note**: This project is currently under active development.

## Project Overview

Universal Multilingual Text-to-Speech is a locally hosted, offline-capable application that generates natural-sounding speech from text in various languages. It leverages the Suno Bark model to provide high-quality audio without relying on cloud APIs or paid services.

## Features

- **Multilingual Support**: Automatically handles input in multiple languages (English, Hindi, Spanish, etc.).
- **Offline Capability**: Fully functional offline after the initial model download.
- **Privacy-Focused**: Runs entirely on your local machine; no data is sent to the cloud.
- **Cost-Free**: Uses open-source models and libraries.

## System Requirements

- **OS**: Windows (tested), Linux, macOS
- **Python**: 3.10+
- **RAM**: 8GB+ recommended (Bark models are memory intensive)
- **Disk Space**: ~5GB+ for models and dependencies
- **Internet**: Required only for the first run to download models.

## Installation

1. **Clone or Download the Project**
   Ensure you have the project files locally.

2. **Set Up Virtual Environment**
   Run the following command in the project root:

   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**

   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**

   ```bash
   venv\Scripts\python app.py
   # Or on Linux/Mac:
   # ./venv/bin/python app.py
   ```

2. **Open the Interface**
   The application will launch in your default web browser (usually at `http://127.0.0.1:7860`).

3. **Generate Speech**
   - Type or paste your text into the text box.
   - Click "Generate Speech".
   - Listen to the output or download the WAV file.

## Troubleshooting

- **First Run Slowness**: The first time you generate speech, the application downloads the Bark models (~5GB+). This depends on your internet speed and might take 10-30 minutes. Please be patient.
- **Slow Generation**: If you are running on CPU, generation can be slow. A 10-second audio clip might take 10-30 seconds to generate depending on your CPU.
- **Out of Memory**: If the app crashes with memory errors, try closing other applications. 8GB+ RAM is recommended.

## Architecture

1. **User Interface (Gradio)**:

   - Captures text input.
   - Sends text to the backend TTS engine.
   - Plays back the generated audio.

2. **Backend (Bark TTS)**:

   - `tts/bark_tts.py`: Handles model loading and inference.
   - Uses `suno/bark` small/large models (auto-downloaded to cache).
   - Generates raw audio arrays.

3. **Utilities**:
   - `utils/audio_utils.py`: Saves audio to WAV format.

## Model Information (Why Bark?)

We use **Suno Bark** because:

- It is **Transformer-based**, allowing for highly realistic, non-monotonic speech.
- It supports **multilingual generation** out of the box without needing separate models for each language.
- It can generate **non-speech sounds** (laughs, sighs) if prompted, adding realism.
- It is **fully open-source** (MIT license).

> **Note on Memory**: By default, this app uses the **Small** version of Bark models to ensure it runs on standard consumer hardware (preventing Out-Of-Memory errors).

## Offline Usage

After the first successful generation (which downloads the models), the application works completely offline.
The models are stored in your local cache (`~/.cache/suno/` by default).

## Limitations

- **Generation Speed**: On CPU, generation can be slow (roughly 1:1 or slower depending on hardware).
- **VRAM/RAM Usage**: Requires significant memory (~4GB+ VRAM if GPU used, or decent system RAM).
- **Long Text**: Long text might need to be split into sentences for best results.

## License

MIT License
