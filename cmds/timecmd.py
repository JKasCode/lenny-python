import datetime

def func():
    time = datetime.datetime.now()
    print("The time is " + time.strftime("%H") + ":" + time.strftime("%M"))
    print("Today is " + time.strftime("%A") + ", " + time.strftime("%d") + " " + time.strftime("%B"))
