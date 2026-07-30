import json, time, requests
STREAM_URL = "https://httpbun.com" 
def process_inventory_stream():
    print("📡 Connecting to inventory data stream...")
    try:
        response = requests.get(STREAM_URL, stream=True, timeout=10)
        response.raise_for_status()
        print("✅ Connection established. Processing live data lines:\n")
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                print(f"📦 [Stream Ingested] Packet ID: {data.get('id')}")
                time.sleep(0.5)
    except requests.exceptions.RequestException as e:
        print(f"❌ Stream connection failed: {e}")
if __name__ == "__main__":
    process_inventory_stream()
