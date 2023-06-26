import time
import os


def clear():
    """System clear"""
    os.system("cls" if os.name == "nt" else "clear")


clear()
while True:
    try:
        workTime = int(input("Insert time to work (in minutes):"))
        break
    except:
        clear()
        print("Insert a number")

clear()
while True:
    try:
        restTime = int(input("Insert time to rest (in minutes):"))
        break
    except:
        clear()
        print("Insert a number")

clear()
print(workTime, restTime)
