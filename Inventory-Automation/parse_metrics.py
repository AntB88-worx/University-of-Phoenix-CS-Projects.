import csv
import os

# ==============================================================================
# LIGHTWEIGHT PROCEDURAL SCRIPTING PIPELINE
# ==============================================================================
# WHY IT IS HERE: 
# Unlike 'inventory_manager.py' which uses heavy OOP architecture for long-term 
# scale, this file is deliberately engineered as a pure procedural script. 
# For rapid, straight-through File I/O parsing, a lean procedural approach 
# eliminates object allocation overhead, resulting in faster execution speeds 
# for simple utility automated workflows.
# ==============================================================================

def process_inventory(file_path, report_path):
    # Introductory message explaining the purpose and personal context of the script
    print("==========================================================")
    print("     INVENTORY AUTOMATION: Operational Logic Engine       ")
    print("==========================================================")
    print("💡 What this is: An automated data pipeline that reads a")
    print("   raw business spreadsheet (CSV file) and extracts major")
    print("   operational and financial metrics from it.")
    print("\n📝 Personal Note: I wanted to test out file reading and")
    print("   data processing techniques learned in class by building")
    print("   a fully automated reporting mechanism!")
    print("==========================================================\n")
    
    # WHAT YOU ARE SEEING: Defensive programming and safety checks.
    # HOW IT OPERATES: Verifies file path availability before trying to open data stream.
    print(f"🔄 Step 1: Checking for data source connection to '{file_path}'...")
    if not os.path.exists(file_path):
        print(f"❌ Error: The data file '{file_path}' was not found.")
        return
    print("✅ File found successfully. Ingesting records...\n")

    # WHAT YOU ARE SEEING: Accumulators and local caching structures.
    # WHY THEY ARE HERE: These primitive data types act as fast registers to track 
    # warehouse stats on-the-fly inside memory while looping through the file rows.
    total_items = 0
    total_value = 0.0
    category_counts = {}
    low_stock_alerts = []

    try:
        # WHAT YOU ARE SEEING: Streaming File Reader.
        # HOW IT OPERATES: Ingesting raw strings and parsing them into active variables.
        # It uses memory buffering to read the file row-by-row rather than crashing 
        # the system by loading a massive file all at once.
        print("🔄 Step 2: Parsing rows and calculating business valuations...")
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                qty = int(row['quantity'])
                cost = float(row['unit_cost'])
                category = row['category']
                name = row['item_name']
                
                # Calculations Engine
                total_items += qty
                total_value += (qty * cost)
                category_counts[category] = category_counts.get(category, 0) + qty
                
                # Business Logic Feature: Flag low stock threshold (< 50 units)
                if qty < 50:
                    low_stock_alerts.append(f"{name} ({qty} units left)")

        # WHAT YOU ARE SEEING: Formatted output layer for business operations reporting.
        print("\n📊 Step 3: Processed Operational Metrics:")
        print(f"  📦 Total Units in Stock: {total_items:,}")
        print(f"  💰 Total Inventory Valuation: ${total_value:,.2f}")
        
        print("\n🗂️ Stock Breakdown by Category:")
        for cat, count in category_counts.items():
            print(f"  ▪️ {cat}: {count} units")
            
        # WHAT YOU ARE SEEING: Automated downstream alert generation.
        # HOW IT OPERATES: Opens an independent out-stream to write a separate text file.
        print(f"\n🔄 Step 4: Generating automated file output to '{report_path}'...")
        with open(report_path, mode='w', encoding='utf-8') as report:
            report.write("⚠️ AUTOMATED LOW STOCK ALERT REPORT ⚠️\n")
            report.write("=========================================\n")
            if low_stock_alerts:
                for alert in low_stock_alerts:
                    report.write(f"- ALERT: {alert}\n")
            else:
                report.write("All stock levels healthy.\n")
        print(f"✅ Success! Restock report compiled and exported.")
            
    # WHAT YOU ARE SEEING: Robust error handling layers.
    # WHY THEY ARE HERE: Ensures that bad data inputs or missing columns halt the 
    # system gracefully instead of throwing ugly, unreadable code traces at users.
    except (ValueError, KeyError) as e:
        print(f"❌ Data Parsing Error: Ensure CSV fields match. Details: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        
    print("\n==========================================================")
    print("                   Processing Complete                    ")
    print("==========================================================")

# ==============================================================================
# MAIN SYSTEM EXECUTION ROUTINE
# ==============================================================================
if __name__ == "__main__":
    # Local configurations targeting repository layout data files
    data_file = "inventory_manifest.csv"
    output_report = "restock_report.txt"
    
    process_inventory(data_file, output_report)
