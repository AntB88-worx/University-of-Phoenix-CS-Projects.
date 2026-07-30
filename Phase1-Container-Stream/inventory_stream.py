import time
import random
import json
import sys

def generate_mock_inventory_stream():
    """Simulates a real-time live data stream of warehouse inventory adjustments."""
    items = ["Laptop Pro 14", "Quantum Mouse", "OLED Monitor 27", "Mechanical Keyboard", "USB-C Hub"]
    warehouses = ["WH-East", "WH-West", "WH-Central"]
    
    print("🛰️  Inventory Data Stream Active... Press Ctrl+C to stop.\n")
    print(f"{'TIMESTAMP':<20} | {'ITEM':<20} | {'LOCATION':<10} | {'DELTA':<6} | {'STATUS'}")
    print("-" * 70)

    try:
        while True:
            # Create a mock data packet
            payload = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "item": random.choice(items),
                "warehouse": random.choice(warehouses),
                "quantity_delta": random.randint(-50, 100)
            }
            
            # Simulate real-time processing logic
            status = "📉 RESTOCK REQ" if payload["quantity_delta"] < 0 else "📈 INBOUND"
            
            # Print the streamed data packet in real time
            print(f"{payload['timestamp']:<20} | {payload['item']:<20} | {payload['warehouse']:<10} | {payload['quantity_delta']:+6} | {status}")
            sys.stdout.flush()  # Forces immediate printing inside Docker containers
            
            # Wait 1.5 seconds before streaming the next item packet
            time.sleep(1.5)
            
    except KeyboardInterrupt:
        print("\n🛑 Stream stopped by user. Cleaning up resources...")

if __name__ == "__main__":
    generate_mock_inventory_stream()
