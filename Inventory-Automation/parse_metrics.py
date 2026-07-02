import csv
import os

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
    
    # Direction Line: Verifying file path availability
    print(f"🔄 Step 1: Checking for data source connection to '{file_path}'...")
    if not os.path.exists(file_path):
        print(f"❌ Error: The data file '{file_path}' was not found.")
        return
    print("✅ File found successfully. Ingesting records...\n")

    total_items = 0
    total_value = 0.0
    category_counts = {}
    low_stock_alerts = []

    try:
        # Direction Line: Ingesting raw strings and parsing them into active variables
        print("🔄 Step 2: Parsing rows and calculating business valuations...")
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                qty = int(row['quantity'])
                cost = float(row['unit_cost'])
                category = row['category']
                name = row['item_name']
                
                # Calculations
                total_items += qty
                total_value += (qty * cost)
                category_counts[category] = category_counts.get(category, 0) + qty
                
                # Business Logic Feature: Flag low stock threshold (< 50 units)
                if qty < 50:
                    low_stock_alerts.append(f"{name} ({qty} units left)")

        # Print final formatted metrics to the screen
        print("\n📊 Step 3: Processed Operational Metrics:")
        print(f"  📦 Total Units in Stock: {total_items:,}")
        print(f"  💰 Total Inventory Valuation: ${total_value:,.2f}")
        
        print("\n🗂️ Stock Breakdown by Category:")
        for cat, count in category_counts.items():
            print(f"  ▪️ {cat}: {count} units")
            
        # Automate low stock alert file generation
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
            
    except (ValueError, KeyError) as e:
        print(f"❌ Data Parsing Error: Ensure CSV fields match. Details: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        
    print("\n==========================================================")
    print("                   Processing Complete                    ")
    print("==========================================================")

if __name__ == "__main__":
    data_file = "inventory_manifest.csv"
    output_report = "restock_report.txt"
    process_inventory(data_file, output_report)
