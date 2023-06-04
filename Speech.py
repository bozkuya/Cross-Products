
import speech_recognition as sr


def convert_speech_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source)

        audio = r.listen(source)

        print("Recognizing Now .... ")

        # recognize speech using google
        try:
            print("You have said \n" + r.recognize_google(audio, language = 'en-US' ))
            print("Audio Recorded Successfully \n ")

        except Exception as e:
            print("Error :  " + str(e))
            return "None"

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())

        print()
        return r.recognize_google(audio, language = 'en-US')

