import datetime
import time
import os

# 1. Set the target date for your first day of class (e.g., June 29, 2026 at 7:00 AM)
# Format: datetime.datetime(Year, Month, Day, Hour, Minute)
target_date = datetime.datetime(2026, 6, 29, 7, 0)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    # 2. Get the current exact time right now
    now = datetime.datetime.now()

    # 3. Calculate the time difference between now and the target date
    time_left = target_date - now

    # 4. If the date hasn't passed yet, break down the remaining time
    if time_left.total_seconds() > 0:
        days = time_left.days
        hours, remainder = divmod(time_left.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # 5. Print a clean visual countdown display
        print("=========================================")
        print("     COUNTDOWN TO CORECS CLASSES         ")
        print("=========================================")
        print("  {days} Days | {hours} Hours | {minutes} Minutes | {seconds} Seconds  ")
        print("=========================================")
        print("\n(Press Ctrl + C in the terminal to stop)")
    else:
        print("🎉 The semester has offically started! Good Luck! 🎉")
        break

    # 6. Pause for 1 second before refreshing the countdown loop
    time.sleep(1) 