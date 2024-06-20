"""
Flock
Clock
"""

import time

print("")
print("---")
print("Flock - The Clock App")
print("---")
print("")

elapsed = 0
finalElapsedMins = 0
finalElapsedSecs = 0
modeSelection = False
stopwatch = False

while modeSelection == False:
    print("Modes:")
    print("1. Stopwatch")
    print("")
    modeOption = input("Choose what mode you want to use corresponding to its number: ")

    if modeOption == "1":
        modeSelection = True
        stopwatch = True
    else:
        print("")
        print("Use the number in front of the modes to choose the modes.")
        print("")
        
if stopwatch == True:
    print("")
    print("")
    print("")

while stopwatch == True:
    
    if finalElapsedSecs < 10:
        print(f"Time Elapsed: {finalElapsedMins}:0{finalElapsedSecs}")
    else:
        print(f"Time Elapsed: {finalElapsedMins}:{finalElapsedSecs}")
    
    
    
    elapsed = elapsed + 1
    finalElapsedMins = elapsed // 60
    finalElapsedSecs = elapsed % 60
    time.sleep(1)
    
