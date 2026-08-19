import ollama
from memory import Memory

class Brain:
    def __init__(self):
        self.mem = Memory()


    def think(self, text):
        history = self.mem.load()
        messages=[
               {
                    "role": "system",
                    "content": "You are JARVIS, a real assistant serving Tejaswa. Be helpful and brief."
                    },
        ]
        for item in history:
            messages.append({"role": "user", "content": item["user"]})
            messages.append({"role": "assistant", "content": item["jarvis"]})
        
        #new message
        messages.append({"role": "user", "content": text})
        
        response = ollama.chat(model = "llama3", messages=messages)

        reply = response["message"]["content"]

        #save memory
        self.mem.save(text, reply)

        return reply
    
    