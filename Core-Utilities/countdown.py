import sys
import time

def run_countdown_timer(total_seconds):
    print("\n⏳ Commencing Countdown Sequence...")
    time.sleep(1) # Give the user a moment to prepare
    
    # Core Loop: Work backward from the target time down to zero
    while total_seconds >= 0:
        # Calculate structural minutes and leftover seconds
        mins, secs = divmod(total_seconds, 60)
        
        # Format the time layout into a standard MM:SS string
        timer_display = f"{mins:02d}:{secs:02d}"
        
        # Direction Line: Print on the same line ('\r') and clear previous text
        # This keeps the output compact instead of filling the whole screen
        print(f"\r⏱️ Time Remaining: [{timer_display}] ", end="", flush=True)
        
        # Pause the system for exactly 1 second, then subtract from our timer
        time.sleep(1)
        total_seconds -= 1
        
    # Terminal alert indicator when sequence completes successfully
    print("\n\n🔔 BEEP! BEEP! Time is up!")
    print("==========================================================")

if __name__ == "__main__":
    # Introductory message explaining the purpose and personal context of the script
    print("==========================================================")
    print("         UTILITIES: Precision Countdown Timer             ")
    print("==========================================================")
    print("💡 What this is: An interactive terminal timer designed   ")
    print("   to format mathematical increments into an active MM:SS ")
    print("   countdown readout without cluttering the screen.       ")
    print("\n📝 Personal Note: I wanted to test custom user inputs,")
    print("   mathematical mod operations, and real-time screen ")
    print("   row overrides in my Python utility portfolio!")
    print("==========================================================\n")

    try:
        # Ingest and sanitize input values to prevent crashes
        user_input = input("⏰ Enter the countdown duration in total seconds: ")
        target_time = int(user_input)
        
        if target_time <= 0:
            print("❌ Input Error: Please enter a number greater than zero.")
        else:
            run_countdown_timer(target_time)
            
    except ValueError:
        print("❌ Type Error: Mismatched format. Please enter a whole number.")
    except KeyboardInterrupt:
        print("\n\n🛑 Timer aborted early by user.")
        print("==========================================================")


"Upgrade countdown timer with input sanitization and line-override loops"
