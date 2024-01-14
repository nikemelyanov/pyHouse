import speech_recognition as sr

class Garri():
    sr.LANGUAGE = 'ru-RU'
    
    def __init__(self, keyword: str, listening: bool):
        self.keyword = keyword
        self.listening = listening
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        
    def sayHello(self) -> None:
        from gtts import gTTS
        text = "Привет!"
        tts = gTTS(text=text, lang='ru', tld='com')
        tts.save("./mp3/output.mp3")

        from pydub import AudioSegment
        from pydub.playback import play

        sound = AudioSegment.from_file("./mp3/output.mp3", format="mp3")
        play(sound)

    def sayOk(self) -> None:
        from gtts import gTTS
        
        text = "хорошо!"
        tts = gTTS(text=text, lang='ru', tld='com')
        tts.save("./mp3/output.mp3")

        from pydub import AudioSegment
        from pydub.playback import play

        sound = AudioSegment.from_file("./mp3/output.mp3", format="mp3")
        play(sound)

    def sending_a_recorded_voice(self, text: str) -> None:
        import requests
        url = 'http://127.0.0.1:8000'
        text = text
        data = {'text': text}
        
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('Запрос успешно отправлен')
        else:
            print('Произошла ошибка при отправке запроса')

    def listen_for_keyword(self, keyword: str) -> bool:
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print('Слушаю...')
            audio = self.r.listen(source)
        
        try:
            text = self.r.recognize_google(audio, language='ru-RU')
            if keyword in text.lower():
                print('Кодовое слово обнаружено!')
                return True
            else:
                return False
        except sr.UnknownValueError:
            print('Не удалось распознать речь')
            return False

    def record_text(self, duration: int) -> None:
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print('Запись пошла...')
            audio = self.r.record(source, duration=duration)
        
        try:
            text = self.r.recognize_google(audio, language='ru-RU')
            print(f'Вы сказали: {text}')
            self.sending_a_recorded_voice(text) # --------- SENDING
        except sr.UnknownValueError:
            print('Не удалось распознать речь')