from alsa_error_handler import error_handler_wrapper
from garri import Garri

error_handler_wrapper()

garri = Garri(keyword='звук', listening=True)

while garri.listening:
    if garri.listen_for_keyword('звук'):
        garri.sayHello()
        garri.record_text(5)
        garri.sayOk()
        # garri.listening = False







