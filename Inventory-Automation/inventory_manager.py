import csv

# Upgraded to an easily modifiable list of tracking dictionaries
inventory_list = [
    {"sku": "SKU-1001", "item_name": "Heavy Duty Pallets", "current_stock": 45, "reorder_threshold": 50, "unit_cost": 15.00},
    {"sku": "SKU-1002", "item_name": "Industrial Stretch Wrap", "current_stock": 120, "reorder_threshold": 30, "unit_cost": 25.50},
    {"sku": "SKU-1003", "item_name": "Cardboard Boxes (Med)", "current_stock": 12, "reorder_threshold": 40, "unit_cost": 1.75},
    {"sku": "SKU-1004", "item_name": "Packing Tape Rolls", "current_stock": 85, "reorder_threshold": 25, "unit_cost": 3.25}
]

def analyze_inventory():
    print("==================================================")
    print("📦 UPGRADED DISPATCH & INVENTORY REPORT")
    print("==================================================\n")
    
    reorder_alerts = 0
    total_reorder_cost = 0.0
    
    for item in inventory_list:
        sku = item['sku']
        name = item['item_name']
        stock = item['current_stock']
        threshold = item['reorder_threshold']
        cost = item['unit_cost']
        
        if stock <= threshold:
            variance = threshold - stock
            item_total_cost = variance * cost
            total_reorder_cost += item_total_cost
            
            print(f"🚨 ALERT | {sku} ({name}) is low!")
            print(f"  -> Stock: {stock} | Threshold: {threshold}")
            print(f"  -> Order Quantity: {variance} units @ ${cost:.2f} each")
            print(f"  -> Projected Expense: ${item_total_cost:.2f}\n")
            reorder_alerts += 1
        else:
            print(f"✅ SECURE | {sku} ({name}) Level Optimal ({stock}/{threshold})")
            
    print("==================================================")
    print(f"📋 SUMMARY: {reorder_alerts} items require procurement.")
    print(f"💰 TOTAL ESTIMATED RESTOCK COST: ${total_reorder_cost:.2f}")
    print("==================================================")

if __name__ == "__main__":
    analyze_inventory()
