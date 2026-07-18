import calendar
import os
import re
import time
from datetime import datetime

def display_logistics_planner(target_year, highlight_date=None, operational_milestone=None):
    cal = calendar.TextCalendar(calendar.SUNDAY)
    # Generate the standard 12-month raw text grid for the target year
    full_year_text = cal.formatyear(target_year, w=2, l=1, c=6, m=3)
    
    # 1. FIXED HOLIDAY MATRIX: Define federal shipping carrier holiday dates (Month, Day)
    CARRIER_HOLIDAYS = {
        "January":,    # New Year's Day
        "July":,       # Independence Day
        "November":,  # Thanksgiving (Approximate fixed shipping block)
        "December": [25]   # Christmas Day
    }

    # 2. MONTH-BY-MONTH PARSING LOGIC: Inject operations metadata dynamically
    for month_num in range(1, 13):
        month_name = calendar.month_name[month_num]
        if month_name not in full_year_text:
            continue
            
        # Isolate the text block of the specific month to prevent accidental global text replacement
        months_split = full_year_text.split(month_name, 1)
        left_side, right_side = months_split[0], months_split[1]
        
        # Split right side again to ensure we only manipulate the current month's grid row block
        next_months = list(calendar.month_name)[month_num+1:]
        break_point = len(right_side)
        for next_m in next_months:
            if next_m in right_side:
                break_point = right_side.find(next_m)
                break
        
        current_month_block = right_side[:break_point]
        remaining_months_block = right_side[break_point:]

        # A. HIGHLIGHT LIVE CLOCK: Wrap today's active date in bracket indicators [ ]
        if highlight_date and target_year == highlight_date.year and highlight_date.month == month_num:
            current_day = highlight_date.day
            current_month_block = re.sub(rf"\b{current_day}\b", f"[{current_day}]", current_month_block, count=1)

        # B. OVERLAY MILESTONE TARGETS: Wrap custom operations milestones in braces { }
        if operational_milestone and target_year == operational_milestone.year and operational_milestone.month == month_num:
            m_day = operational_milestone.day
            current_month_block = re.sub(rf"\b{m_day}\b", f"{{{m_day}}}", current_month_block, count=1)

        # C. CARRIER HOLIDAY INJECTION: Tag freight shipping deadlines with an 'H' prefix
        if month_name in CARRIER_HOLIDAYS:
            for holiday_day in CARRIER_HOLIDAYS[month_name]:
                current_month_block = re.sub(rf"\b{holiday_day}\b", f"H{holiday_day}", current_month_block, count=1)

        # Reconstruct the layout string cleanly after handling the rules
        full_year_text = left_side + month_name + current_month_block + remaining_months_block

    # 3. PEAK SEASON CAPACITY ALERT: Flag high-risk distribution months (November & December)
    # Uses text substitution to add alert tags directly to the month text headers
    full_year_text = full_year_text.replace("November", "November ⚠️[PEAK CAPACITY]")
    full_year_text = full_year_text.replace("December", "December ⚠️[PEAK CAPACITY]")

    print("\n=========================================================================")
    print(f"             🏭 ENTERPRISE SUPPLY CHAIN CAPACITY PLANNER: {target_year}  ")
    print("=========================================================================")
    print(full_year_text)
    print("=========================================================================")
    print(" 🛠️  LEGEND:  [xx] = Current Day | {xx} = Target Milestone | Hxx = Carrier Holiday")
    print("=========================================================================")

if __name__ == "__main__":
    print("==========================================================")
    print("       LOGISTICS UTILITIES: Annual Capacity Planner       ")
    print("==========================================================\n")
    
    today = datetime.now()
    
    # Ingest custom milestone input to show real-world time-horizon path planning
    milestone_date = None
    ms_input = input("🎯 Enter a specific operational deadline date (MM-DD-YYYY) or Enter to skip: ").strip()
    if ms_input:
        try:
            milestone_date = datetime.strptime(ms_input, "%m-%d-%Y")
            print(f"✅ Milestone loaded: '{milestone_date.strftime('%B %d, %Y')}' locked into engine.")
        except ValueError:
            print("⚠️  Invalid format. Proceeding with baseline calendar display.")
            time.sleep(1)

    # Clear terminal screen dynamically across architectures
    os.system('cls' if os.name == 'nt' else 'clear')
    display_logistics_planner(today.year, highlight_date=today, operational_milestone=milestone_date)
    
    # Allow safe exploratory testing for future years
    try:
        user_year = input("\n📆 Enter a different 4-digit year to audit future capacity (or Enter to exit): ").strip()
        if user_year:
            searched_year = int(user_year)
            if 1 <= searched_year <= 9999:
                os.system('cls' if os.name == 'nt' else 'clear')
                display_logistics_planner(searched_year, highlight_date=today, operational_milestone=milestone_date)
    except ValueError:
        print("❌ Format Error: Please enter a valid numerical 4-digit year.")
