
import serial
import time
import speech_recognition as sr
import random


arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)


def servo_positioner(hor, ver):

    arduino.write(bytes(hor, 'utf-8')),
    time.sleep(0.05)
    arduino.write(bytes(ver, 'utf-8'))
    time.sleep(0.05)

def convert_speech_text():

    inp_hor = 10            # 10 degree offset is needed for the pan tilt
    inp_ver = 20            # default vertical angle

    r = sr.Recognizer()

    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")

        # recognize speech using google

        try:
            print("You have said \n" + r.recognize_google(audio, language = 'en-US' ))
            print("Audio Recorded Successfully \n ")



        except Exception as e:
            print("Error :  " + str(e))

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())
            if (r.recognize_google(audio, language = 'en-US') == "left"):
                print("Motors are turning left")
                inp_hor -= 30
            elif (r.recognize_google(audio, language = 'en-US') == "right"):
                print("Motors are turning right")
                inp_hor += 30
            elif (r.recognize_google(audio, language = 'en-US' ) == "turn up"):
                print("Motors are facing upwards")
                inp_ver += 20
            elif (r.recognize_google(audio, language = 'en-US' ) == "turn down"):
                print("Motors are facing downwards")
                inp_ver -= 20
            elif (r.recognize_google(audio, language = 'en-US' ) == "front"):
                print("Motors are giving frontspin")
            elif (r.recognize_google(audio, language = 'en-US' ) == "stop"):
                print("Motors are stopping")
            elif (r.recognize_google(audio, language = 'en-US' ) == "faster"):
                print("Motors are increasing the speed")
            elif (r.recognize_google(audio, language = 'en-US' ) == "slower"):
                print("Motors are decreasing the speed")
            else:
                print("Detected word is not valid!")
                convert_speech_text()

            return inp_hor, inp_ver



while True:
    hori_angle, vert_angle = convert_speech_text()

    #num_hor = input("Enter a horizontal angle (-90,90): ")
    #num_ver = input("Enter a vertical angle (0,90): ")

    #value = servo_positioner(str(hori_angle), str(vert_angle))
    print(hori_angle, vert_angle)


