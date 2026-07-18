import os
import time
from datetime import datetime, timedelta, timezone

def run_digital_clock():
    # -----------------------------------------------------------------
    # CONFIGURATION: Map core logistics hubs to strict UTC offsets
    # -----------------------------------------------------------------
    HUBS = {
        "1": ("DFW Hub (Central)", -6),    
        "2": ("LAX Gateway (Pacific)", -8), 
        "3": ("JFK Cargo (Eastern)", -5)    
    }
    
    print("==========================================================")
    print("       🏭 SUPPLY CHAIN AUTOMATION: OPERATIONAL CLOCK      ")
    print("==========================================================\n")
    print("Select Target Logistics Hub:")
    for key, (name, _) in HUBS.items():
        print(f" [{key}] {name}")
    
    choice = input("Enter selection (1-3, Default '1'): ").strip()
    hub_name, hub_offset = HUBS.get(choice, HUBS["1"])
    
    # INPUT: Define the target deadline window (SLA) for order dispatching
    sla_input = input("\nSet Dispatch SLA Window Target (HH:MM, Default '18:30'): ").strip() or "18:30"
    sla_hours, sla_minutes = map(int, sla_input.split(":"))
    
    # SIMULATION: Fast-forward hours to stress-test future warehouse shifts
    sim_input = input("\nHours to fast-forward shift (-12 to +12, Default '0'): ").strip()
    hours_offset = int(sim_input) if sim_input.lstrip('-').isdigit() else 0
    
    print("\n⏰ Booting engine... Press [Ctrl + C] to exit.")
    time.sleep(1)

    try:
        while True:
            # Refresh terminal frame seamlessly across Windows and Linux/macOS
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # 1. TIME ZONE MATH: Calculate base hub time using strict UTC calculation
            utc_now = datetime.now(timezone.utc)
            hub_now = utc_now + timedelta(hours=hub_offset)
            
            # 2. SHIFT SIMULATION MATH: Inject offset variables into the runtime state
            simulated_now = hub_now + timedelta(hours=hours_offset)
            
            # 3. SLA COUNTDOWN LOGIC: Project dynamic remaining window deadlines
            target_sla = simulated_now.replace(hour=sla_hours, minute=sla_minutes, second=0, microsecond=0)
            if target_sla < simulated_now:
                target_sla += timedelta(days=1) # Target moves to tomorrow if shift window passed
                
            sla_diff = target_sla - simulated_now
            sla_hours_left = sla_diff.seconds // 3600
            sla_mins_left = (sla_diff.seconds % 3600) // 60
            sla_secs_left = sla_diff.seconds % 60
            
            # 4. BUSINESS LOGIC MATRIX: Flag critical warnings if time window drops under 2 hours
            status_alert = "⚠️  CRITICAL REORDER LIMIT" if sla_hours_left < 2 else "✅ Flow Normal"
            
            # OUTPUT DISPLAY BANNERS
            print("=========================================================")
            print(f"       🏭 SUPPLY CHAIN CONTROL TOWER: {hub_name.upper()} ")
            print("=========================================================")
            print(f"  📅 Target Date : {simulated_now.strftime('%A, %B %d, %Y')}")
            print(f"  🕒 Hub Wall Time: {simulated_now.strftime('%I:%M:%S %p')} (UTC{hub_offset:+})")
            if hours_offset != 0:
                print(f"  🎛️  SIMULATOR  : Active ({hours_offset:+amp;h shift offset applied})")
            print("---------------------------------------------------------")
            print(f"  📦 Target SLA Window: {target_sla.strftime('%I:%M %p')}")
            print(f"  ⏳ Time Remaining   : {sla_hours_left:02d}h {sla_mins_left:02d}m {sla_secs_left:02d}s")
            print(f"  📢 System Status    : {status_alert}")
            print("=========================================================")
            
            time.sleep(1) # Infinite event loop tick rate
            
    except KeyboardInterrupt:
        print("\n\n🛑 Engine execution safely interrupted by developer.")

if __name__ == "__main__":
    run_digital_clock()
