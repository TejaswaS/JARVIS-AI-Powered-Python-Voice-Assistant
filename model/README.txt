I would add a section like:

🎙️ Vosk Speech Recognition Model

JARVIS uses a large Vosk English speech-recognition model based on the Appen UHV-OTS Speech/Kaldi model for accurate English speech recognition.

Model: Accurate Universal English Model (Callcenter + Wideband)
Base: Appen Kaldi Speech Model
Size: ~2.66 GB

Due to its large size, the speech-recognition model is not included in this GitHub repository.

Download the model separately and extract it into the model/ directory:

JARVIS/
├── main.py
├── model/
│   ├── am/
│   ├── conf/
│   ├── graph/
│   └── ...
└── ...

Once the model is placed in the correct directory, JARVIS can use it for offline speech recognition.