from moviepy.editor import VideoFileClip
import speech_recognition as sr
from translate import Translator


PATH = "D:\\Program Files\\programmingLabs\\test\\"
STORE = sr.Recognizer()


def convert_to_mp3(file_video, file_audio):
    video = VideoFileClip(file_video)
    audio = VideoFileClip(file_video).audio
    audio.write_audiofile(file_audio)
    audio.close()
    video.close()


def create_text_audio(audio):
    with sr.AudioFile(audio) as source:
        audio_speech = STORE.record(source)
    print("Text: ")
    try:
        text = STORE.recognize_sphinx(audio_speech)
        print("finished..")
        return text
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


def translate_in_ru():
    translator = Translator(from_lang="en", to_lang="ru")
    result = ""
    tmp = ""
    counter = 0
    words = create_text_audio(f'{PATH}audio.wav').split()
    for word in range(len(words)):
        if counter >= 62:
            result += translator.translate(f'{tmp}')
            tmp = ""
            counter = 0
            continue
        tmp += words[word] + " "
        counter += 1
    with open('text.doc', 'w') as file:
        file.write(result)

if __name__ == '__main__':
    # converttomp3(f'{PATH}v.mp4', f'{PATH}audio.wav')
    translate_in_ru()
