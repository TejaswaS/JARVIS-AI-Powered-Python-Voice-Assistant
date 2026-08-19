from audio.offline_recognizer import OfflineRecognizer
from ai.brain import Brain
from commands.executor import CommandExecutor
from voice.speaker import Speaker
import time
from overlay import run_overlay
import threading

threading.Thread(target=run_overlay, daemon=True).start()

listener = OfflineRecognizer()
brain = Brain()
executor = CommandExecutor()
speaker = Speaker()
processing = False

while True:
    text = listener.listen()
    if processing:
        time.sleep(0.1)
        continue

    

    if not text:
        continue

    processing = True

    print("You:", text)

    action = executor.run(text)

    if action:
        speaker.speak(action)
    else:
        reply = brain.think(text)
        print("Jarvis:", reply)
        speaker.speak(reply)

    time.sleep(1.5)  # cooldown after speaking
    processing = False
