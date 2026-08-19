import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer
import numpy as np

class OfflineRecognizer:
    def __init__(self):
        self.model = Model(r"C:\Users\TEJASWA SHARMA\OneDrive\Desktop\Projects\JARVIS\model")
        self.q = queue.Queue()
        self.samplerate = 16000
        self.rec = KaldiRecognizer(self.model, self.samplerate)
        self.rec.SetWords(True)
        self.rec.SetPartialWords(True)


    def callback(self, indata, frames, time, status):
        audio = np.frombuffer(indata, dtype=np.int16)
        audio = (audio * 2).astype(np.int16) # amplify signal
        self.q.put(audio.tobytes())
        

    def listen(self):
        print("Listening... speak now")

        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=self.callback,
    ):
            while True:
                data = self.q.get()

                if self.rec.AcceptWaveform(data):
                    result = json.loads(self.rec.Result())
                    text = result.get("text", "").strip()

                    # ignore noise but KEEP listening
                    if len(text.split()) < 2:
                        continue

                    print("Detected:", text)
                    return text
