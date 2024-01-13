from ctypes import *
from contextlib import contextmanager
import pyaudio

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)

with noalsaerr():
    p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)



# import speech_recognition as sr

# r = sr.Recognizer()
# mic = sr.Microphone()

# sr.LANGUAGE = 'ru-RU'

# with mic as source:
#     r.adjust_for_ambient_noise(source)
#     print('Запись пошла...')
#     data = r.record(source, duration=5)
#     text = r.recognize_google(data, language='ru-RU')
#     print(f'Вы сказали {text}')



# from openai import OpenAI
# import pyaudio
# import wave

# client = OpenAI(
#     api_key="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",
# )


# def recognize_speech(path):
#     audio_file= open(path, "rb")
#     transcript = client.audio.translations.create(
#         model="whisper-1", 
#         file=audio_file,
#         response_format="text"
#     )

#     print(f'Вы сказали: {transcript.lower()}')

# def record_audio_to_file(file_path, record_seconds=5):
#     # Установка параметров аудиозаписи
#     chunk = 1024  # Записываемые блоки
#     format = pyaudio.paInt16  # Формат аудио
#     channels = 1  # Количество каналов
#     rate = 44100  # Частота дискретизации

#     p = pyaudio.PyAudio()

#     # Открытие потока для записи
#     stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

#     print("Recording...")

#     frames = []

#     # Запись данных в блоки за указанное время
#     for i in range(0, int(rate / chunk * record_seconds)):
#         data = stream.read(chunk)
#         frames.append(data)

#     print("Finished recording.")

#     # Остановка и закрытие потока
#     stream.stop_stream()
#     stream.close()
#     p.terminate()

#     # Сохранение записи в файл
#     wf = wave.open(file_path, 'wb')
#     wf.setnchannels(channels)
#     wf.setsampwidth(p.get_sample_size(format))
#     wf.setframerate(rate)
#     wf.writeframes(b''.join(frames))
#     wf.close()

#     return file_path

# path = record_audio_to_file("output.wav", 5)

# recognize_speech(path)


import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
sr.LANGUAGE = 'ru-RU'

def sending_a_recorded_voice(text):
    import requests
    url = 'http://127.0.0.1:8000'
    text = text
    data = {'text': text}
    
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('Запрос успешно отправлен')
    else:
        print('Произошла ошибка при отправке запроса')

def listen_for_keyword(keyword):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Слушаю...')
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='ru-RU')
        if keyword in text.lower():
            print('Кодовое слово обнаружено!')
            return True
        else:
            return False
    except sr.UnknownValueError:
        print('Не удалось распознать речь')
        return False

def record_text(duration):
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print('Запись пошла...')
        audio = r.record(source, duration=duration)
    
    try:
        text = r.recognize_google(audio, language='ru-RU')
        print(f'Вы сказали: {text}')
        sending_a_recorded_voice(text) # --------- SENDING
    except sr.UnknownValueError:
        print('Не удалось распознать речь')

keyword = 'гарри' 
listening = True

while listening:
    if listen_for_keyword(keyword):
        record_text(5)
        listening = False
