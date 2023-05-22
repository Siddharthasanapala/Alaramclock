import time
import playsound
current_time=time.localtime()
present_time=str(current_time.tm_hour)+":"+str(current_time.tm_min)+":"+str(current_time.tm_sec)
print("Welcome to ALARAM \n 1 -> Morning wakeup alaram \n 2 -> General alaram \n")
choice=int(input("Please select your alaram type :"))
ALARAM_TIME=str(input("Enter the time to set alaram :"))
alaram="not rang"

while alaram=="not rang":
    current_time=time.localtime()
    present_time=str(current_time.tm_hour)+":"+str(current_time.tm_min)+":"+str(current_time.tm_sec)
    if present_time==ALARAM_TIME and choice==1:
        print("Its High Time Wake up..!")
        playsound.playsound("C:/Users/SIDDHARTHA/Music/cockwakeup.mp3")
        alaram="Alaram rang"
    if present_time==ALARAM_TIME and choice==2:
        print("Your Time Arrived")
        playsound.playsound("C:/Users/SIDDHARTHA/Music/chukkalachunni.mp3")
        alarams="Alaram rang"
