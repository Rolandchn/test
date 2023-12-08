

import datetime
import playsound 

from IA import AI


eris = AI()

commands = {}

command = ""
while command != "goodbye":
    command = eris.listen()

    if command == "Hey Eris":
        eris.wake()

    elif command == "Give me the time":
        eris.say(datetime.datetime.now())
        eris.sleep()

    elif command == "Give me the weather":
        eris.sleep()

    elif command == "Magic":
        playsound.playsound("audio_test/Eris_magic.mp3")
        eris.sleep()


eris.say("Goodbye Rudeus!")