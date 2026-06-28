import time
import os

# This loop will run forever, updating the 
while True:
    # 1. Clear the terminal screen so the clock stays on a single line
    # (Use 'cls' for Windows environments, 'clear' for Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

    # 2. Grab the current local system time and format it beautifully
    current_time = time.strftime("%H:%M:%S")

    # 3. Print the time to the screen with a clean visual border
    print("====================")
    print(f"   CURRENT TIME:  {current_time}  ")
    print("====================")
    print("\n(Press Ctrl + C in terminal stop the clock)")

    # 4. Tell the computer to pause for exactly 1 second before looping again
    time.sleep (1)