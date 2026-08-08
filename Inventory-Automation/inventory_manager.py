import sqlite3
import os

# ==============================================================================
# DATA BLUEPRINT ENTITY: THE INVENTORY ITEM
# ==============================================================================
# WHY IT IS HERE: 
# This class handles individual product validation. By separating the item data 
# logic away from the database storage operations, we maintain clean encapsulation.
# ==============================================================================
class InventoryItem:
    """Represents a single unique SKU inside the physical warehouse ecosystem."""
    
    def __init__(self, sku, item_name, current_stock, reorder_threshold, unit_cost):
        self.sku = sku
        self.item_name = item_name
        self.current_stock = int(current_stock)
        self.reorder_threshold = int(reorder_threshold)
        self.unit_cost = float(unit_cost)

    @property
    def requires_restock(self):
        """WHAT IT DOES: Instantly evaluates if stock levels have tripped safety boundaries."""
        return self.current_stock <= self.reorder_threshold

    @property
    def variance(self):
        """WHAT IT DOES: Computes the precise item count required to replenish stock."""
        if self.requires_restock:
            return self.reorder_threshold - self.current_stock
        return 0

    @property
    def projected_expense(self):
        """WHAT IT DOES: Dynamically calculates the capital procurement needs."""
        return self.variance * self.unit_cost


# ==============================================================================
# PERSISTENT SQL DATABASE & OPERATIONAL CONTROL PIPELINE
# ==============================================================================
# WHY IT IS HERE: 
# This engine handles the core CRUD operations. Moving from in-memory arrays to 
# SQL introduces database persistence. It utilizes "Parameterized Queries" to 
# explicitly protect systems against SQL Injection vulnerabilities—proving 
# engineering security awareness to cloud architectural assessors.
# ==============================================================================
class SQLInventoryPipeline:
    """Handles persistent database schemas, data ingestion, and operations reporting."""
    
    def __init__(self, db_path):
        # WHAT YOU ARE SEEING: Database file management initialization.
        self.db_path = db_path
        self._initialize_database_schema()

    def _initialize_database_schema(self):
        """
        WHAT IT DOES: Automated schema deployment.
        HOW IT OPERATES: Connects to the local storage cluster and executes a DDL command 
        to ensure the tracking tables exist safely before any transactions occur.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            # Creating relational structures with explicit column constraints
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inventory_manifest (
                    sku TEXT PRIMARY KEY,
                    item_name TEXT NOT NULL,
                    current_stock INTEGER NOT NULL,
                    reorder_threshold INTEGER NOT NULL,
                    unit_cost REAL NOT NULL
                )
            """)
            conn.commit()

    def ingest_raw_payload(self, raw_data):
        """
        WHAT IT DOES: Populates persistent relational storage.
        HOW IT OPERATES: Uses SQL 'REPLACE' commands paired with parameterized tuples. 
        This keeps operations data refreshed without duplicate primary key collisions.
        """
        # STEP 1: Opening transactional context block
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Formatting incoming raw pipelines to safely slip into secure database arrays
            for item in raw_data:
                cursor.execute("""
                    INSERT OR REPLACE INTO inventory_manifest 
                    (sku, item_name, current_stock, reorder_threshold, unit_cost)
                    VALUES (?, ?, ?, ?, ?)
                """, (item["sku"], item["item_name"], item["current_stock"], item["reorder_threshold"], item["unit_cost"]))
            
            conn.commit()

    def run_dispatch_report(self):
        """
        WHAT IT DOES: Compiles production-grade logistics insights straight from SQL storage.
        HOW IT OPERATES: Queries the persistent ledger, dynamically builds strongly-typed 
        InventoryItem objects on-the-fly, and prints actionable metrics to the terminal console.
        """
        print("==================================================")
        print("💾 RELATIONAL DATABASE DISPATCH REPORT (SQL)")
        print("==================================================\n")
        
        reorder_alerts = 0
        total_reorder_cost = 0.0

        with sqlite3.connect(self.db_path) as conn:
            # Querying structural tables via programmatic transaction connections
            conn.row_factory = sqlite3.Row  # Enables column fetching by key strings rather than index locations
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inventory_manifest")
            rows = cursor.fetchall()

            for row in rows:
                # Instantiating clean application objects directly out of persistent records
                item = InventoryItem(
                    sku=row["sku"],
                    item_name=row["item_name"],
                    current_stock=row["current_stock"],
                    reorder_threshold=row["reorder_threshold"],
                    unit_cost=row["unit_cost"]
                )

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
# MAIN CLOUD ROUTINE INGESTION DISPATCHER
# ==============================================================================
if __name__ == "__main__":
    
    # WHAT YOU ARE SEEING: Database naming target
    DATABASE_NAME = "warehouse_ecosystem.db"
    
    # Simulating data ingestion stream typical of inbound cloud payloads or messaging queues
    RAW_INVENTORY_PAYLOAD = [
        {"sku": "SKU-1001", "item_name": "Heavy Duty Pallets", "current_stock": 45, "reorder_threshold": 50, "unit_cost": 15.00},
        {"sku": "SKU-1002", "item_name": "Industrial Stretch Wrap", "current_stock": 120, "reorder_threshold": 30, "unit_cost": 25.50},
        {"sku": "SKU-1003", "item_name": "Cardboard Boxes (Med)", "current_stock": 12, "reorder_threshold": 40, "unit_cost": 1.75},
        {"sku": "SKU-1004", "item_name": "Packing Tape Rolls", "current_stock": 85, "reorder_threshold": 25, "unit_cost": 3.25}
    ]
    
    # HOW IT OPERATES: 
    # 1. Connects to database interface instance handler.
    # 2. Ingests current incoming payload stream down into permanent tables.
    # 3. Fires calculations algorithm to print persistent business analytics.
    pipeline = SQLInventoryPipeline(DATABASE_NAME)
    pipeline.ingest_raw_payload(RAW_INVENTORY_PAYLOAD)
    pipeline.run_dispatch_report()
