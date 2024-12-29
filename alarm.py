from datetime import datetime
from time import sleep

def alarm_clock():
    alarm_hour = int(input("Set hour: "))
    alarm_minute = int(input("Set minutes: "))
    am_pm = input("am or pm? ").lower()

    if am_pm == "pm":
        alarm_hour += 12

    while True:
        now = datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Wake Up!")
            break

        sleep(1)
alarm_clock()