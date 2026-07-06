import pyttsx3
import datetime

#date and time setup
remainder = True
hour = int(datetime.datetime.now().hour)
min = int(datetime.datetime.now().minute)
time = datetime.datetime.now().strftime("%aday:[ %H :%M %p] ")
print(time)

#task to do
task = [input("enter your task...")]
set_hour,set_min = input("enter your time in Hour:Min ").split(":")
set_hour = int(set_hour)
set_min = int(set_min)

#check for remainder
def condition():
    global remainder
    while remainder:
        #date and time setup
        hour = int(datetime.datetime.now().hour)
        min = int(datetime.datetime.now().minute)

        if (set_hour == hour) and (set_min == min):
            print(task)
            engine = pyttsx3.init()
            engine.say("TASK TIME")
            for i in range(3):
                engine.say("Hurry up,Time Do Work")
                engine.runAndWait()
            remainder = False

#notification of remainder
while remainder:
    condition()