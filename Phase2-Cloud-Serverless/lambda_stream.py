import json
import time
import urllib.request
from urllib.parse import urlparse

def lambda_handler(event, context):
    print("🛰️ Ingesting Real-World Logistics Weather Telemetry!")
    
    # Live REST API endpoint pulling from the Memphis International Airport (FedEx Global Hub)
    api_url = "https://open-meteo.com"
    
    try:
        # Remediate Bandit B310: Explicitly validate the URL scheme before connection
        parsed_url = urlparse(api_url)
        if parsed_url.scheme not in ('http', 'https'):
            raise ValueError(f"Disallowed URL scheme: {parsed_url.scheme}")

        # Perform live HTTP network fetch
        with urllib.request.urlopen(api_url, timeout=5) as response:
            raw_data = json.loads(response.read().decode())
            
        current_metrics = raw_data.get("current", {})
        temperature = current_metrics.get("temperature_2m", 20.0)
        humidity = current_metrics.get("relative_humidity_2m", 50)
        
        # Build live, production-grade telemetry payload
        payload = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "item": "Global Logistics Temperature Monitor",
            "warehouse": "FedEx-Memphis-Hub",
            "quantity_delta": int(temperature), # Pass temperature value as our delta metrics metric
            "status": "📉 ANOMALY CHK" if temperature > 30 or temperature < 0 else "📈 OPTIMAL"
        }
        
        print(f"📦 Successfully Ingested Payload: {json.dumps(payload)}")
        return {"statusCode": 200, "body": json.dumps(payload)}
        
    except Exception as e:
        print(f"❌ Public API Ingestion Failure: {e}")
        return {"statusCode": 500, "body": str(e)}
