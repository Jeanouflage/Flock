# Flock - The Python Clock App
# https://github.com/Jeanouflage/Flock

from time import sleep
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


print("""
---
Flock - The Clock App
---
""")

elapsed = 0
modeSelection = False
stopwatch = False
timer = False
time = False
days = 0
hrs = 0
mins = 0
secs = 0
totalSecs = -1
parsedTime = [days, hrs, mins, secs]
timezones = {
    "1": "UTC",
    "2": "Europe/Malta",
    "3": "Europe/London",
    "4": "Europe/Paris",
    "5": "Europe/Berlin",
    "6": "America/New_York",
    "7": "America/Chicago",
    "8": "America/Los_Angeles",
    "9": "Asia/Tokyo",
    "10": "Asia/Shanghai",
    "11": "Asia/Kolkata",
    "12": "Australia/Sydney"
}

timezoneSupport = True

try:
    ZoneInfo("UTC")
except ZoneInfoNotFoundError:
    timezoneSupport = False


while modeSelection == False:
    print("Modes:")
    print("1. Stopwatch")
    print("2. Timer")
    modeOption = input("Choose a Mode (1/2): ")

    # This only works in Python 3.10 or above, but in my opinion, it is more efficient
    match modeOption:
        case "1":
            modeSelection = True
            stopwatch = True
        case "2":
            modeSelection = True
            timer = True
        case "3":
            modeSelection = True
            time = True
        case default:
            print("\nInvalid Mode\n")
        
if stopwatch or timer or time:
    print("\n\n\n")

while stopwatch:
    secs = format((elapsed % 60), '02d')
    mins = format((elapsed // 60) % 60, '02d')
    hrs = format((elapsed // 3600) % 24, '02d')
    days = format((elapsed // 3600 // 24), '02d')

    parsedTime = [days, hrs, mins, secs]

    if days == "00": parsedTime.remove(days)

    print(f"Time Elapsed: {':'.join(parsedTime)}")
    
    
    
    elapsed += 1
    sleep(1)
    
if timer:
    days = int(input("Days: "))
    hrs = int(input("Hours: "))
    mins = int(input("Minutes: "))
    secs = int(input("Seconds: "))
    totalSecs = days * 86400 + hrs * 3600 + mins * 60 + secs
    print("")
    if totalSecs == 0:
        timer = False

while timer:
    if totalSecs:
        timer = False
    
while totalSecs > 0:
    days = totalSecs // 86400
    hrs = (totalSecs % 86400) // 3600
    mins = (totalSecs % 3600) // 60
    secs = totalSecs % 60
    
    if days == 0 and hrs == 0:
        print(f"Time left: {mins:02d}:{secs:02d}")
    elif days == 0:
        print(f"Time left: {hrs:02d}:{mins:02d}:{secs:02d}")
    else:
        print(f"Time left: {days:02d}:{hrs:02d}:{mins:02d}:{secs:02d}")
        
    totalSecs -= 1


    sleep(1)
    
if totalSecs == 0:
    print("\nTimer is finished")



