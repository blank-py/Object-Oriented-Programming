# File name: task9.py
# Author: Jesse Malinen
# Description: Actual code based on pseudocode from task 9.

import time

class Alarm:
    
    def __init__(self):
        self.alarm_hour = input("Enter the hour: ")
        self.alarm_minute = input("Enter the minute: ")
        print("Alarm set for: " + self.alarm_hour + ":" + self.alarm_minute)
        
def main():
    set_alarm = Alarm()
    
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        now = current_time.split(":")
        
        if set_alarm.alarm_hour == now[0] and set_alarm.alarm_minute == now[1]:
            print("Wake up! Time is: " + current_time)
            break
        else:
            print(current_time)
            time.sleep(1)
            
main()