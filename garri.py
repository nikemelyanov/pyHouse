import speech_recognition as sr

from speech_synthesis import Speech_synthesis

class Garri(Speech_synthesis):
    sr.LANGUAGE = 'ru-RU'
    
    def __init__(self, keyword: str, listening: bool):
        self.keyword = keyword
        self.listening = listening
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def sending_a_recorded_voice(self, text: str) -> None:
        if text.lower() == 'включи свет':
            print('sendeng... свет будет включен')
            # import requests
            # url = 'http://127.0.0.1:8000'
            # text = text
            # data = {'text': text}
            
            # response = requests.post(url, json=data)
            # if response.status_code == 200:
            #     print('Запрос на включения света успешно отправлен')
            # else:
            #     print('Произошла ошибка при отправке запроса на включения света')
        

    def listen_for_keyword(self, keyword: str) -> bool:
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)
            print('Слушаю...')
            audio = self.r.listen(source)
        
        try:
            text = self.r.recognize_google(audio, language='ru-RU')
            if keyword in text.lower():
                print(f'кодовое слово - {keyword} обнаружено!')
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