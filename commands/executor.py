import webbrowser 
import os 

class CommandExecutor:
    def run(self, text):
        text = text.lower()
        
        #Websites Commands
        sites = {
            "youtube": "https://youtube.com",
            "chatgpt": "https://chat.openai.com",
            "gemini": "https://gemini.google.com",
            "google classroom": "https://classroom.google.com",
        }
        for name, url, in sites.items():
            if name in text:
                webbrowser.open(url)
                return f"Opening {name}"
            

        # apps commands
        apps = {
            "vs code": "code",
            "file explorer": "explorer",
            "word": "winword",
        }
        for name, cmd in apps.items():
            if name in text:
                os.system(cmd)
                return f"Opening {name}"
            
        if "whatsapp" in text:
            os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
            return "Opening WhatsApp"

            
        return None