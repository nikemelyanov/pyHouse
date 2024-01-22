import threading
import time
from alsa_error_handler import error_handler_wrapper
from garri import Garri

def GarriWorking(): 
    error_handler_wrapper()
    garri = Garri(keyword='звук', listening=True)

    while garri.listening:
        if garri.listen_for_keyword('звук'):
            garri.sayHello()
            garri.record_text(5)
            garri.sayOk()
            # garri.listening = False

def threading2():
    while True:
        print('hi')
        time.sleep(1)

thread = threading.Thread(target=GarriWorking)
thread2 = threading.Thread(target=threading2)

thread.start()
thread2.start()