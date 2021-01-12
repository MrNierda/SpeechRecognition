import speech_recognition as sr
# from operation_produced import main
import operation_produced
import language

def recognize_audio(spoken_language=language.Language.FR):
    """
    Activate microphone to listen to the user
    Return the audio as a string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print('Audio listened!')

    try:
        text = r.recognize_google(audio, language=spoken_language)
        print("Text: " + text)
        return text
    except:
        print('Audio not recognized!')

def language_selection():
    languages = language.get_languages()
    print(f'Say the language you want to use among those {list(languages.keys())}')
    selected_language = recognize_audio()
    
    if selected_language not in list(languages.keys()):
        print("I didn't find the desired language")
        language_selection()

    print(f'\nSelected language is {selected_language}')
    commands_for_lang = list(language.get_command_for_lang(selected_language).values())
    print(f'\nHere the existing command for the current language {commands_for_lang}')

    return languages.get(selected_language)

def main():
    print('Starting...')
    selected_language = language_selection()
    print(f'\nYou selected {selected_language}')
    
    print('\nWhat do you want to do?')
    activity = recognize_audio(selected_language)
    operation_produced.main(activity)


if __name__ == '__main__':
    main()