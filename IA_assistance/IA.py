


import time
import pyaudio
import pyttsx3
import speech_recognition as sr

from enum import Enum




class State(Enum):
    IDLE = 0
    ACTIVE = 1


class AI:
    __name = "Eris"
    __skill = {}

    def __init__(self, name = None):
        self.engine = pyttsx3.init()
        self.recogniser = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.state = State.IDLE

        if name is not None:
            self.__name = name

    
    @property
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self, value):
        sentence = f"Hello, my name is {self.__name}"
        self.__name = value
        self.say(sentence)


    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()


    def listen(self):
        print("Say something...")

        with self.microphone as source: 
            self.recogniser.adjust_for_ambient_noise(source) # wait a seconde to adjust the ambient noice
            audio = self.recogniser.listen(source)
        
        if self.state == State.ACTIVE:
            print("Got it!")

            try:
                # recognize_sphinx can be use offline (no internet)
                phrase = self.recogniser.recognize_google(audio, show_all=False)
                sentence = f"Got it, you said: {phrase}"
                self.say(sentence)

            except:
                error_message = "Sorry, I didn't understand"
                print(error_message)

                self.say(error_message)
            
            return phrase
        
    
    def wake(self):
        self.state = State.ACTIVE


    def sleep(self):
        self.state = State.IDLE