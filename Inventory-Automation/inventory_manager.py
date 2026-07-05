import csv

# ==============================================================================
# DATA ब्लू-प्रिंट / BLUEPRINT ENTITY: THE INVENTORY ITEM
# ==============================================================================
# WHY IT IS HERE: 
# Instead of treating warehouse items as simple text strings or abstract items 
# in a flat list, this class bundles an item's data (attributes) and its 
# business rules (methods) together. This represents the core OOP principle 
# of "Encapsulation". It makes sure each item knows how to audit itself.
# ==============================================================================
class InventoryItem:
    """Represents a single unique SKU inside the physical warehouse ecosystem."""
    
    def __init__(self, sku, item_name, current_stock, reorder_threshold, unit_cost):
        # HOW IT OPERATES: Initializes the physical data parameters for a warehouse node.
        # Types are explicitly cast to ensure data integrity during downstream calculations.
        self.sku = sku
        self.item_name = item_name
        self.current_stock = int(current_stock)
        self.reorder_threshold = int(reorder_threshold)
        self.unit_cost = float(unit_cost)

    @property
    def requires_restock(self):
        """
        WHAT IT DOES: Evaluates stock safety parameters.
        WHY IT'S A PROPERTY: Acts like a dynamic variable. It instantly compares 
        physical inventory against baseline safety thresholds without needing manual loop checks.
        """
        return self.current_stock <= self.reorder_threshold

    @property
    def variance(self):
        """
        WHAT IT DOES: Determines the exact procurement order size.
        HOW IT OPERATES: Computes the precise gap between target stock boundaries 
        and reality. Returns 0 if stock is completely secure.
        """
        if self.requires_restock:
            return self.reorder_threshold - self.current_stock
        return 0

    @property
    def projected_expense(self):
        """
        WHAT IT DOES: Calculates capital requirements for procurement teams.
        HOW IT OPERATES: Dynamically multiplies item financial costs by the target variance gap.
        """
        return self.variance * self.unit_cost


# ==============================================================================
# OPERATIONAL PIPELINE & METRICS CONTROL ENGINE
# ==============================================================================
# WHY IT IS HERE: 
# This class acts as the 'Manager' or 'Pipeline'. It isolates data storage 
# and structural report generation away from individual items. This achieves 
# "Separation of Concerns" (SoC)—if your database changes in the future, 
# you only update this engine, leaving your core InventoryItem logic untouched.
# ==============================================================================
class InventoryAutomationPipeline:
    """Handles data ingestion, physical inventory arrays, and automated dispatch reports."""
    
    def __init__(self, raw_data):
        # WHAT YOU ARE SEEING: An internal list designed to hold object instances rather than dicts.
        self.inventory = []
        self._load_data(raw_data)

    def _load_data(self, data):
        """
        WHAT IT DOES: Converts raw incoming data strings into strongly-typed objects.
        HOW IT OPERATES: Iterates over the raw payload, instantiates an InventoryItem 
        for each entry, and appends it to our structured pipeline tracking array.
        """
        for item in data:
            self.inventory.append(
                InventoryItem(
                    sku=item["sku"],
                    item_name=item["item_name"],
                    current_stock=item["current_stock"],
                    reorder_threshold=item["reorder_threshold"],
                    unit_cost=item["unit_cost"]
                )
            )

    def run_dispatch_report(self):
        """
        WHAT IT DOES: Generates the ultimate physical-to-digital metrics report.
        HOW IT OPERATES: Cycles through all loaded tracking nodes, instantly checks 
        their restock properties, and prints tailored operational alerts or secure summaries.
        """
        print("==================================================")
        print("📦 UPGRADED DISPATCH & INVENTORY REPORT (OOP)")
        print("==================================================\n")
        
        reorder_alerts = 0
        total_reorder_cost = 0.0
        
        # Loop relies entirely on the object properties rather than extracting dict keys manually
        for item in self.inventory:
            if item.requires_restock:
                total_reorder_cost += item.projected_expense
                reorder_alerts += 1
                
                print(f"🚨 ALERT | {item.sku} ({item.item_name}) is low!")
                print(f"  -> Stock: {item.current_stock} | Threshold: {item.reorder_threshold}")
                print(f"  -> Order Quantity: {item.variance} units @ ${item.unit_cost:.2f} each")
                print(f"  -> Projected Expense: ${item.projected_expense:.2f}\n")
            else:
                print(f"✅ SECURE | {item.sku} ({item.item_name}) Level Optimal ({item.current_stock}/{item.reorder_threshold})")
                
        print("==================================================")
        print(f"📋 SUMMARY: {reorder_alerts} items require procurement.")
        print(f"💰 TOTAL ESTIMATED RESTOCK COST: ${total_reorder_cost:.2f}")
        print("==================================================")


# ==============================================================================
# MAIN SYSTEM EXECUTION ROUTINE
# ==============================================================================
if __name__ == "__main__":
    
    # WHAT YOU ARE SEEING: A mock database payload imitating your warehouse manifest metrics.
    # By separating this from the architecture above, the system is fully modular.
    RAW_INVENTORY_PAYLOAD = [
        {"sku": "SKU-1001", "item_name": "Heavy Duty Pallets", "current_stock": 45, "reorder_threshold": 50, "unit_cost": 15.00},
        {"sku": "SKU-1002", "item_name": "Industrial Stretch Wrap", "current_stock": 120, "reorder_threshold": 30, "unit_cost": 25.50},
        {"sku": "SKU-1003", "item_name": "Cardboard Boxes (Med)", "current_stock": 12, "reorder_threshold": 40, "unit_cost": 1.75},
        {"sku": "SKU-1004", "item_name": "Packing Tape Rolls", "current_stock": 85, "reorder_threshold": 25, "unit_cost": 3.25}
    ]
    
    # HOW IT OPERATES: 
    # 1. We instantiate the automation pipeline, feeding it our raw records.
    # 2. We trigger the dispatch report function to compile and present our logistics insights.
    pipeline = InventoryAutomationPipeline(RAW_INVENTORY_PAYLOAD)
    pipeline.run_dispatch_report()
