import os
import sys
import time
from datetime import datetime

def run_custom_milestone_counter(target_date, target_label, hourly_fine, handling_buffer_hours):
    # 1. BUFFER CORRECTION: Calculate the absolute drop-dead execution window
    true_deadline = target_date
    buffer_seconds = handling_buffer_hours * 3600
    
    print(f"\n⏳ Booting Risk Tracking Engine for: '{target_label}'...")
    time.sleep(1)

    try:
        while True:
            now = datetime.now()
            time_remaining = true_deadline - now
            total_seconds_left = time_remaining.total_seconds()

            # SLA BREACH: Handle what happens when the operational milestone is missed
            if total_seconds_left <= 0:
                print(f"\n\n🚨 SLA BREACH: Milestone '{target_label}' deadline passed!")
                print(f"💰 Financial Loss Incurred: ${hourly_fine:,.2f} baseline breach penalty.")
                print("==========================================================")
                break

            # Deconstruct calendar metrics
            days = time_remaining.days
            hours, remainder = divmod(time_remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            # 2. RISK MATRIX LOGIC: Dynamically assess system risk levels based on time remaining
            total_hours_left = total_seconds_left / 3600
            
            if total_hours_left <= handling_buffer_hours:
                risk_status = "❌ BREACH IMMINENT (Inside Buffer Window)"
            elif total_hours_left <= 2:
                risk_status = "⚠️  CRITICAL RISK (Under 2hr Window)"
            elif total_hours_left <= 24:
                risk_status = "⚡ MODERATE RISK (Under 24hr Window)"
            else:
                risk_status = "✅ LOW RISK (Flow Normal)"

            # 3. FINANCIAL ANALYSIS LAYER: Project compounding financial liability
            current_risk_cost = hourly_fine if total_hours_left <= handling_buffer_hours else 0.00

            # Output tracking metrics cleanly using a single-line terminal rewrite wrapper (\r)
            print(
                f"\r🎯 Time Until {target_label}: [{days}d {hours:02d}h {minutes:02d}m {seconds:02d}s] | "
                f"Status: {risk_status} | Exposure: ${current_risk_cost:,.2f} ", 
                end="", 
                flush=True
            )

            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n🛑 Tracking engine for '{target_label}' safely paused.")

if __name__ == "__main__":
    print("==========================================================")
    print("      LOGISTICS ENGINE: Operational Milestone Analyzer    ")
    print("==========================================================\n")

    # Ingest and validate custom target date structures
    try:
        user_date_input = input("📆 Enter target milestone date (MM-DD-YYYY): ").strip()
        milestone_name = input("🏷️  Enter milestone label (e.g., Target Trailer Pull): ").strip()
        
        # 4. DATA INPUT REFACTORING: Parse string to date object
        target_date = datetime.strptime(user_date_input, "%m-%d-%Y")
        
        # Combine date with end of business day (5:00 PM / 17:00) as a standard logistics anchor
        target_date = target_date.replace(hour=17, minute=0, second=0)

        # Operational business variables
        fine_input = input("💰 Enter SLA breach penalty fee ($ value, e.g., 500): ").strip()
        hourly_fine = float(fine_input) if fine_input.isdigit() else 0.00
        
        buffer_input = input("⏱️  Enter processing buffer time required (Hours, e.g., 3): ").strip()
        handling_buffer_hours = int(buffer_input) if buffer_input.isdigit() else 0

        # Boot engine
        run_custom_milestone_counter(target_date, milestone_name, hourly_fine, handling_buffer_hours)

    except ValueError:
        print("\n❌ Input Error: Data structure invalid. Ensure you enter parameters accurately.")
