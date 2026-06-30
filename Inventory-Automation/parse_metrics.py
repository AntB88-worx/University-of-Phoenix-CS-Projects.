import csv
import os

def process_inventory(file_path):
    print("==========================================================")
    print("     INVENTORY AUTOMATION: Operational Logic Engine       ")
    print("==========================================================")
    
    if not os.path.exists(file_path):
        print(f"❌ Error: The data file '{file_path}' was not found.")
        return

    total_items = 0
    total_value = 0.0
    category_counts = {}

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Core parsing and data conversion logic
                qty = int(row['quantity'])
                cost = float(row['unit_cost'])
                category = row['category']
                
                # Metric calculations
                total_items += qty
                total_value += (qty * cost)
                
                # Category data tracking
                category_counts[category] = category_counts.get(category, 0) + qty

        # Output processed financial and operational metrics
        print("\n📊 Processed Operational Metrics:")
        print(f"📦 Total Units in Stock: {total_items:,}")
        print(f"💰 Total Inventory Valuation: ${total_value:,.2f}")
        
        print("\n🗂️ Stock Breakdown by Category:")
        for cat, count in category_counts.items():
            print(f"  ▪️ {cat}: {count} units")
            
    except (ValueError, KeyError) as e:
        print(f"❌ Data Parsing Error: Ensure CSV fields match. Details: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        
    print("==========================================================")

if __name__ == "__main__":
    # Target the local manifest data file
    data_file = "inventory_manifest.csv"
    process_inventory(data_file)
