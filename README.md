# Python Voice Assistant

This is a Python-based voice assistant that listens to your voice commands, processes them, and performs actions such as playing music, and opening webpages. It uses speech recognition and text-to-speech modules for audio input and output.

## Features

- **Speech Recognition**: Converts your spoken commands into text.
- **Text-to-Speech (TTS)**: Provides voice feedback using `pyttsx3`.
- **Music Playback**: Play music.

## Requirements

Ensure the following Python packages are installed by running:

```bash
pip install -r requirements.txt
```

### List of Required Modules

- `certifi==2024.8.30`
- `cffi==1.17.1`
- `charset-normalizer==3.4.0`
- `idna==3.10`
- `pocketsphinx==5.0.3`
- `PyAudio==0.2.14`
- `pycparser==2.22`
- `pyobjc==10.3.1`
- `pyttsx3==2.98`
- `requests==2.32.3`
- `sounddevice==0.5.1`
- `SpeechRecognition==3.10.4`
- `urllib3==2.2.3`
- `wheel==0.44.0`

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/notaarryan/Voice-Assistant
   cd <repo-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

4. Follow the voice prompts to interact with the assistant.

## Customization

- **Music Controls**: The `music.py` file contains music playback functionalities. You can modify it to add support for other audio formats or services.
- **Speech Recognition**: Adjust the recognition parameters in `main.py` for better accuracy in different environments.

## License

This project is licensed under the [MIT License](LICENSE).
