import csv

# Simulated CSV data structure representing a live warehouse inventory pull
inventory_data = """sku,item_name,current_stock,reorder_threshold
SKU-1001,Heavy Duty Pallets,45,50
SKU-1002,Industrial Stretch Wrap,120,30
SKU-1003,Cardboard Boxes (Med),12,40
SKU-1004,Packing Tape Rolls,85,25
"""

def analyze_inventory():
    print("==================================================")
    print("📦 DISPATCH & INVENTORY AUTOMATION REPORT")
    print("==================================================\n")
    
    # Split the raw payload string into lines for processing
    lines = inventory_data.strip().split('\n')
    reader = csv.DictReader(lines)
    
    reorder_alerts = 0
    
    for row in reader:
        sku = row['sku']
        name = row['item_name']
        stock = int(row['current_stock'])
        threshold = int(row['reorder_threshold'])
        
        # Core operational threshold business logic
        if stock <= threshold:
            variance = threshold - stock
            print(f"🚨 ALERT | {sku} ({name}) is low!")
            print(f"  -> Current Stock: {stock} | Threshold: {threshold}")
            print(f"  -> Action Required: Reorder a minimum of {variance} units.\n")
            reorder_alerts += 1
        else:
            print(f"✅ SECURE | {sku} ({name}) Stock Level Optimal ({stock}/{threshold})")
            
    print("==================================================")
    print(f"📋 SUMMARY: {reorder_alerts} items require immediate procurement.")
    print("==================================================")

if __name__ == "__main__":
    analyze_inventory()
