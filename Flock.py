# Flock - The Python Clock App
# https://github.com/Jeanouflage/Flock

from time import sleep

print("""
---
Flock - The Clock App
---
""")

elapsed = 0
modeSelection = False
stopwatch = False

while modeSelection == False:
    print("Modes:")
    print("1. Stopwatch\n")
    modeOption = input("Choose what mode you want to use corresponding to its number: ")

    # This only works in Python 3.10 or above, but in my opinion, it is more efficient
    match modeOption:
        case "1":
            modeSelection = True
            stopwatch = True
        case default:
            print("\nUse the number in front of the modes to choose the modes.\n")
        
if stopwatch:
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
    