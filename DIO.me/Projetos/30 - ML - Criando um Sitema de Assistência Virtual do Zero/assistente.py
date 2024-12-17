import os
from pathlib import Path
import uuid
import webbrowser
import pyjokes
import speech_recognition as sr
import wikipedia
import pygame

from datetime import datetime
from typing import Optional
from geopy.geocoders import Nominatim
from gtts import gTTS


def get_gtts_obj(text: str, lang: str) -> gTTS:
    try: 
        obj = gTTS(text=text, lang=lang, slow=False)
    except Exception as exc:
        obj = None
        print(f'\nFailed to get a gTTS object. \n\n\t{exc}')
    
    return obj


def speak(text: str, lang: Optional[str] = 'en') -> None:
    # Cria o objeto gTTS
    gTTS_obj = get_gtts_obj(text=text, lang=lang)

    # Caminho do arquivo de áudio
    root_path = Path(__file__).parent
    audio_file = root_path / ('voice.mp3' + str(uuid.uuid4()))

    gTTS_obj.save(audio_file)

    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error reproducing audio.")
    

def get_audio_from_mic() -> str:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1

        r.adjust_for_ambient_noise(source, duration=1)
        
        print('\nYou can talk now...')
        audio = r.listen(source)

        capture: str = ''
        try:
            capture = r.recognize_google_cloud(audio)
            print(f'\nI think you said: {capture}')
        except sr.UnknownValueError:
            speak("\nSorry, I did not get that.")
        except sr.RequestError:
            speak("\nSorry, The service is not available")
    
    return capture.lower()


def manage_action(text: str, *, sub_text: Optional[str] = None) -> None:

    if 'youtube' in text:
        speak("What do you want to search for?")

        if not sub_text:
            query = get_audio_from_mic()
        else:
            query = ''

        if query != '' or sub_text:
            url = f"https://www.youtube.com/results?search_query={query if query != '' else sub_text}"
            webbrowser.get().open(url)
            speak('Opening YouTube')

    if 'search' in text:
        speak("What do you want to search for?")
        if not sub_text:
            query = get_audio_from_mic()
        else:
            query = ''

        if query != '' or sub_text:
            result = wikipedia.summary(query if query != '' else sub_text, sentences=3)
            speak('\nAccording to wikipedia: ')
            print(result)
            speak(result)

    if 'location' in text:
        speak("Where do you want to go")
        if not sub_text:
            query = get_audio_from_mic()
        else:
            query = ''

        if query != '' or sub_text:
            geolocator = Nominatim(user_agent="myGeocoder")

            location = geolocator.geocode(query)
            if location:
                print(location.address)
                speak(location.address)

    elif 'joke' in text:
        speak(pyjokes.get_joke())

    elif 'time' in text:
        formatted_time = datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
        print(f'time: {formatted_time}')
        speak(formatted_time)

    elif 'exit' in text:
        speak("Goodbye, see ya!")
        quit()


if __name__ == '__main__':
    pygame.mixer.init()

    DISABLE_AUDIO = True

    if DISABLE_AUDIO:

        text: str = 'youtube'
        sub_text: str = '3Blue1Brown'
        manage_action(text, sub_text=sub_text)
    
        text: str = 'search'
        sub_text: str = 'galaxies'
        manage_action(text, sub_text=sub_text)

        text: str = 'location'
        sub_text: str = 'new jersey'
        manage_action(text, sub_text=sub_text)

        text: str = 'joke'
        manage_action(text)

        text: str = 'time'
        manage_action(text)

        text: str = 'quit'
        manage_action(text)
    else:
        while True:
            print('\nNow listening...')

            text = get_audio_from_mic()
            manage_action(text)
