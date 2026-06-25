import curses
import datetime
import calendar
import sys

def get_target_date():
    """Prompts user for input and handles all value and format errors."""
    print("=" * 50)
    print("🌟 INTERACTIVE YEARLY COUNTDOWN CALENDAR SETUP")
    print("=" * 50)
    
    while True:
        try:
            print("\nEnter your target countdown date:")
            year = int(input("  Year  (e.g., 2027): ").strip())
            month = int(input("  Month (1-12)       : ").strip())
            day = int(input("  Day   (1-31)       : ").strip())
            
            # This line will raise a ValueError if the date is physically impossible
            target_dt = datetime.date(year, month, day)
            return target_dt
            
        except ValueError:
            print("\n❌ ERROR: Invalid date configuration. Please check your parameters.")
            print("   Ensure month is 1-12, and the day exists within that specific month.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 Program terminated by user.")
            sys.exit(0)

def draw_year_calendar(stdscr, target_date):
    """Curses interface rendering an interactive full-year grid layout."""
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.start_color()
    
    # Theme configuration
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Titles / Grid Headers
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Target Highlight Anchor
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    # Control Hints

    # Initialize calendar viewpoint to focus on the target date's year
    view_year = target_date.year

    while True:
        stdscr.clear()
        max_y, max_x = stdscr.getmaxyx()
        
        # Ensure the terminal terminal window is large enough for a full year grid
        if max_x < 80 or max_y < 28:
            stdscr.addstr(0, 0, "⚠️ Terminal window too small!", curses.color_pair(3) | curses.A_BOLD)
            stdscr.addstr(1, 0, f"Current: {max_x}x{max_y}. Required: min 80x28.")
            stdscr.addstr(2, 0, "Please resize your window to continue...")
            stdscr.refresh()
            key = stdscr.getch()
            if key in (ord('q'), ord('Q')):
                break
            continue

        # 1. Live Countdown Math
        today = datetime.date.today()
        days_diff = (target_date - today).days

        # 2. Top Status Bar UI
        stdscr.addstr(1, 2, f"📅 COUNTDOWN CALENDAR YEAR VIEW: {view_year}", curses.color_pair(1) | curses.A_BOLD)
        stdscr.addstr(2, 2, "=" * 76)
        
        if days_diff > 0:
            status_str = f"🚀 {days_diff} DAYS REMAINING until target date ({target_date.strftime('%m/%d/%Y')}) "
        elif days_diff == 0:
            status_str = f"🥳 TODAY IS THE TARGET DATE! ({target_date.strftime('%m/%d/%Y')}) "
        else:
            status_str = f"⏳ {abs(days_diff)} DAYS PASSED since target date ({target_date.strftime('%m/%d/%Y')}) "
            
        stdscr.addstr(4, 2, status_str, curses.A_REVERSE)
        stdscr.addstr(5, 2, "=" * 76)

        # 3. Generate and Render 3x4 Month Matrix
        # Each column block requires ~25 chars width, each row block requires ~7 lines height
        for m_idx in range(1, 13):
            # Calculate grid coordinates
            row_block = (m_idx - 1) // 3  # 0 to 3
            col_block = (m_idx - 1) % 3   # 0 to 2
            
            start_y = 7 + (row_block * 7)
            start_x = 2 + (col_block * 26)

            # Month Name Header
            m_name = calendar.month_name[m_idx][:3].upper()
            stdscr.addstr(start_y, start_x + 7, f"--- {m_name} ---", curses.color_pair(1))
            
            # Days matrix values
            cal_matrix = calendar.monthcalendar(view_year, m_idx)
            
            for r_num, week in enumerate(cal_matrix):
                for c_num, day in enumerate(week):
                    if day == 0:
                        continue
                    
                    # Highlight target date if view matches target properties
                    if view_year == target_date.year and m_idx == target_date.month and day == target_date.day:
                        stdscr.addstr(start_y + 1 + r_num, start_x + (c_num * 3), f"{day:2}", curses.color_pair(2) | curses.A_BOLD | curses.A_UNDERLINE)
                    else:
                        stdscr.addstr(start_y + 1 + r_num, start_x + (c_num * 3), f"{day:2}")

        # 4. Interactive Bottom Control Menu
        stdscr.addstr(26, 2, "⬅️ Left Arrow: Prev Year   |  ➡️ Right Arrow: Next Year", curses.color_pair(1))
        stdscr.addstr(27, 2, "Press 'Q' to terminate program", curses.color_pair(3))
        stdscr.refresh()

        # 5. Handle Keyboard Controls
        key = stdscr.getch()
        if key == curses.KEY_RIGHT:
            view_year += 1
        elif key == curses.KEY_LEFT:
            view_year -= 1
        elif key in (ord('q'), ord('Q')):
            break

def main():
    # Prompt and clean input first in standard safe terminal loop
    target_date = get_target_date()
    # Handoff to curses for graphical loop
    curses.wrapper(draw_year_calendar, target_date)

if __name__ == "__main__":
    main()