import os
import sys
import time
from datetime import datetime

def run_custom_milestone_counter(target_date, target_label):
    print(f"\n⏳ Initializing real-time tracking engine for: '{target_label}'...")
    time.sleep(1.5)

    try:
        while True:
            # Direction Line: Fetch the current system date and time to find the delta
            now = datetime.now()
            time_remaining = target_date - now

            # If the current system time passes the target date, end the program
            if time_remaining.total_seconds() <= 0:
                print(f"\n\n🎉 CONGRATULATIONS! The milestone '{target_label}' has arrived!")
                print("==========================================================")
                break

            # Deconstruct the time difference into readable calendar metrics
            days = time_remaining.days
            hours, remainder = divmod(time_remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Direction Line: Output tracking calculations smoothly on a single line
            # \r forces the cursor back to the start of the row to override values dynamically
            print(
                f"\r🎯 Time Until {target_label}: [{days}d {hours:02d}h {minutes:02d}m {seconds:02d}s] ", 
                end="", 
                flush=True
            )

            # Pause processing for exactly 1 second before refreshing values
            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n🛑 Tracking engine for '{target_label}' paused by user.")
        print("==========================================================")

if __name__ == "__main__":
    # Introductory message explaining the purpose and personal context of the script
    print("==========================================================")
    print("       UTILITIES: Dynamic Custom Milestone Engine        ")
    print("==========================================================")
    print("💡 What this is: An advanced tracking utility that parses")
    print("   custom user date strings and calculates a live timeline")
    print("   delta down to the second against your system clock.   ")
    print("\n📝 Personal Note: I expanded this script to dynamically")
    print("   process any future user date—like my semester deadline")
    print("   on 12-21-2026—to showcase input parsing and error tracking!")
    print("==========================================================\n")

    print("📋 Instructions: Enter your deadline target using the MM-DD-YYYY format.")
    print("   Example: For the end of the semester, type: 12-21-2026\n")

    # Ingest and validate the custom target date input
    try:
        user_date_input = input("📆 Enter a future milestone date (MM-DD-YYYY): ")
        milestone_name = input("🏷️ Give this milestone a name (e.g., Semester End): ")
        
        from datetime import datetime
# Quick test of the parsing logic to ensure no runtime errors
try:
    test_date = datetime.strptime("12-21-2026", "%m-%d-%Y")
    print(f"Success: {test_date}")
except ValueError:
    print("Error")

    except ValueError:
        print("❌ Format Error: Invalid date structure. Ensure you use the exact MM-DD-YYYY format.")


"Refactor countdown script to dynamically parse custom user dates and labels"
