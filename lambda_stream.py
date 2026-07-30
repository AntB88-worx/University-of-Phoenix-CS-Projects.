import json
import time
import random

def lambda_handler(event, context):
    """
    Standard AWS Lambda entry point. 
    AWS automatically feeds incoming triggers into the 'event' argument.
    """
    print("🛰️ AWS Lambda Logistics Stream Triggered!")
    
    items = ["Laptop Pro 14", "Quantum Mouse", "OLED Monitor 27", "Mechanical Keyboard", "USB-C Hub"]
    warehouses = ["WH-East", "WH-West", "WH-Central"]
    
    payload = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "item": random.choice(items),
        "warehouse": random.choice(warehouses),
        "quantity_delta": random.randint(-50, 100)
    }
    
    payload["status"] = "📉 RESTOCK REQ" if payload["quantity_delta"] < 0 else "📈 INBOUND"
    print(f"📦 Generated Payload: {json.dumps(payload)}")
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Logistics event processed successfully!',
            'data': payload
        })
    }
