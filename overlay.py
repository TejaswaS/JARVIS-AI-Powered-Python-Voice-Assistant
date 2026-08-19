import pystray
from PIL import Image

def run_overlay():
    icon = pystray.Icon("Jarvis", Image.new("RGB", (64, 64), "blue"))
    icon.run()
