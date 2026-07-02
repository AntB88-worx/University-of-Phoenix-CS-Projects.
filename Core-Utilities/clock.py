import os
import time
from datetime import datetime

def run_digital_clock():
    # Introductory message explaining the purpose and personal context of the script
    print("==========================================================")
    print("         UTILITIES: Live Digital Clock Framework          ")
    print("==========================================================")
    print("💡 What this is: A cross-platform terminal clock that     ")
    print("   freshens the console display every second to track time.")
    print("\n📝 Personal Note: I am enhancing my time-utility scripts")
    print("   to learn about infinite event loops, terminal states,")
    print("   and graceful process interruptions using Python!")
    print("==========================================================\n")
    
    print("⏰ Booting clock module... Press Ctrl+C to stop.")
    time.sleep(2) # Give the user a moment to read the introduction

    try:
        # Core Event Loop: Keeps the clock ticking indefinitely
        while True:
            # Direction Line: Cross-platform command to clear old terminal text
            # 'nt' handles Windows operating systems, 'posix' handles macOS and Linux
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Fetch and format current system date and time metrics
            now = datetime.now()
            current_date = now.strftime("%A, %B %d, %Y")
            current_time = now.strftime("%I:%M:%S %p")  # 12-hour AM/PM format
            
            # Print the formatted output screen
            print("=========================================")
            print("         🌐 LIVE SYSTEM TIME 🌐          ")
            print("=========================================")
            print(f"  📅 Date: {current_date}")
            print(f"  🕒 Time: {current_time}")
            print("=========================================")
            print("          Press [Ctrl + C] to Exit       ")
            
            # Pause execution for exactly 1 second before refreshing the loop
            time.sleep(1)
            
    except KeyboardInterrupt:
        # Graceful interruption handling block to prevent messy error code crashes
        print("\n\n🛑 Clock process stopped by user.")
        print("==========================================")

if __name__ == "__main__":
    run_digital_clock()


"Upgrade clock framework with cross-platform screen clearing"
