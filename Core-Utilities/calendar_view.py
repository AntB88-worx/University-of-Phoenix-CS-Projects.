import calendar
import os
import re
import time
from datetime import datetime

def display_full_year_calendar(target_year, highlight_date=None):
    # Set up a text calendar starting on Sunday
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # Generate the standard 12-month raw text grid for the target year
    full_year_text = cal.formatyear(target_year, w=2, l=1, c=6, m=3)
    
    # Core Logic Feature: If the year matches our current year, highlight today's date
    if highlight_date and target_year == highlight_date.year:
        current_day = highlight_date.day
        month_name = highlight_date.strftime("%B") # e.g., "July"
        
        # Split the grid at the target month name to isolate it safely
        if month_name in full_year_text:
            months_split = full_year_text.split(month_name, 1)
            left_side = months_split[0]
            right_side = months_split[1]
            
            # Look for the current day digit inside this month's text block.
            # Handles padding so days like '2' match ' 2 ' and don't break '22'
            day_pattern = rf"\b{current_day}\b"
            
            # Replace the plain digit with a distinct bracket visual anchor inside the right side
            highlighted_right_side = re.sub(day_pattern, f"[{current_day}]", right_side, count=1)
            
            # Reconstruct the layout cleanly as a single string
            full_year_text = left_side + month_name + highlighted_right_side

    print("\n=========================================================================")
    print(f"               📅 FULL 12-MONTH ACADEMIC CALENDAR MATRIX                 ")
    print("=========================================================================")
    print(full_year_text)
    print("=========================================================================")

if __name__ == "__main__":
    # Introductory message explaining the purpose and personal context of the script
    print("==========================================================")
    print("         UTILITIES: 12-Month Academic Planner             ")
    print("==========================================================")
    print("💡 What this is: A terminal dashboard that structures an   ")
    print("   entire annual calendar matrix and uses string logic    ")
    print("   to isolate and highlight the current day.               ")
    print("\n📝 Personal Note: I updated this tool to display a complete")
    print("   12-month overview so I can visually map out my whole   ")
    print("   academic year at a glance!")
    print("==========================================================\n")

    # Fetch live clock metrics right now
    today = datetime.now()
    
    print(f"🔄 Step 1: Connecting to system clock... Highlighting today's date.")
    time.sleep(1.5)
    
    # Clear screen to show the clean year layout
    os.system('cls' if os.name == 'nt' else 'clear')
    display_full_year_calendar(today.year, highlight_date=today)
    
    print(f"\n💡 Notice: Today's date is wrapped in brackets [ ] within your current month.")
    print("\n📋 Custom Target Search:")
    print("   Want to plan out a different year? (Example: 2027)")
    
    # Handle user inputs safely using a try/except rule block
    try:
        user_year_input = input("📆 Enter a 4-digit target year (or press Enter to skip): ").strip()
        if user_year_input:
            searched_year = int(user_year_input)
            
            if searched_year < 1 or searched_year > 9999:
                print("❌ Input Error: Please enter a standard calendar year.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"🔍 Displaying full planning layout for requested year: {searched_year}")
                display_full_year_calendar(searched_year, highlight_date=today)
                
    except ValueError:
        print("❌ Type Error: Mismatched format. Please enter a valid numerical year.")
        
    print("\n🏁 Annual calendar processing complete.")
    print("==========================================================")


"Update calendar view to output full 12-month grid with dynamic day highlighting"
