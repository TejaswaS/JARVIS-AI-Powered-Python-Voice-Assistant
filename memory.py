import json
import os

class Memory:
    def __init__(self):
        self.file = "memory.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f)

    def load(self):
        with open(self.file, "r") as f:
            return json.load(f)
        
    def save(self, text, reply):
        data = self.load()
        data.append({"user": text, "jarvis": reply})

        with open(self.file, "w") as f:
            json.dump(data[-10:], f) #keep last 10 messages 


 