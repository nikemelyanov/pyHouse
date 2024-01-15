from gtts import gTTS

from pydub import AudioSegment
from pydub.playback import play

class Speech_synthesis():
    def sayHello(self) -> None:
        # text = "Привет, я Оля твоя рабыня, прошу вас на коленях, дайте мне комманду что-то сделать по дому!"
        text = "Слушаю!"
        tts = gTTS(text=text, lang='ru', tld='com')
        tts.save("./mp3/output.mp3")

        sound = AudioSegment.from_file("./mp3/output.mp3", format="mp3")
        play(sound)

    def sayOk(self) -> None:
        text = "Секунду..."
        tts = gTTS(text=text, lang='ru', tld='com')
        tts.save("./mp3/output.mp3")

        sound = AudioSegment.from_file("./mp3/output.mp3", format="mp3")
        play(sound)