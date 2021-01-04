#Yafet Assefa
#Intern Project
# Voice Assistant
import speech_recognition as sr
import pyttsx3 as p
from YoutubeAutomation import *
from MovieAutomation import *
from WikipediaAutomation import *
from MovieRecommendations import *

# RECOGNIZER CLASS MAKE INSTANCE USING RECOGNISOR CLASS
# Starting Convo
r1 = sr.Recognizer()  # use recognizer class
engine = p.init()
engine.say("Hello Human, How are you doing to day?")
engine.runAndWait()

with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    print("Hello Human, how are you today?")
    audio = r1.listen(source)

    #text = r1.listen(source)

    try:
        recognised_text = r1.recognize_google(audio)  # Google api recogniser
        print(recognised_text)
        # if recognised_text == "play":
        #   music()
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

    # Instructions
    engine.say("What do you want me to do?")
    engine.runAndWait()

    # Assigning Instructions
    r2 = sr.Recognizer()  # (different instances for recognizers) use recognizer class
    with sr.Microphone() as source:
        r2.adjust_for_ambient_noise(source)
        audio = r2.listen(source)

        try:
            instruction = r2.recognize_google(audio)  # Google api recogniser
            print(recognised_text)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

    # Fetching info from the web
    r3 = sr.Recognizer()  # (different instances for recognizers) use recognizer class
    if "information" in instruction:
        engine.say("information about what?")
        engine.runAndWait()

    with sr.Microphone as source1:
        audio2 = r3.listen(source1)  # recognizes users voice
        try:
            information = r3.recognize_google(audio2)
            bot = Information()
            bot.get_info(information)

        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")

        # Rating Movies
        r4 = sr.Recognizer()
        if "review" in instruction:
            engine.say("Sure Human, What is the name of the movie? ")
            engine.runAndWait()

            with sr.Microphone as source2:
                audio3 = r4.listen(source2)  # recognizes users voice
                try:
                    rating = r4.recognize_google(audio3)
                    bot = Movie()
                    bot.ReviewMovie(rating)

                except sr.UnknownValueError:
                    print("")
                except sr.RequestError as e:
                    print("")

    # Play Music
    r5 = sr.Recognizer()  # (different instances for recognizers) use recognizer class
    if "music" in instruction:
        engine.say("Okay human, Which song shall I play ")
        engine.runAndWait()

        with sr.Microphone as source3:
            audio4 = r5.listen(source3)  # recognizes users voice
            try:
                video = r5.recognize_google(audio4)
                bot = Information()
                bot.play(video)
            except sr.UnknownValueError:
                print("")
            except sr.RequestError as e:
                print("")

    # Movie Recommendation
    if "recommendation" in instruction:
        engine.say("Sure Human, Here are the List you can choose from ")
        engine.runAndWait()
        bot = Recommedation()
        bot.Recommendation_Info()

'''
    # Copied and paste it again
    text1 = r.listen(source)

    try:
        recognised_text1 = r.recognize_google(text1)  # Google api recogniser
        print(recognised_text1)

        if recognised_text1== "play music":
            music()

    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")

        #play a music
        #take a queue and call a function(like automation)
'''
