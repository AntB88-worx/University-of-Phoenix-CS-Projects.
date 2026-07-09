import socket

def analyze_search_engine_dns():
    # Search engine domains to analyze
    domains = ["googlebot.com", "bing.com", "duckduckgo.com"]
    
    print("🌐 IT Student Network Analysis: Search Engines & DNS")
    print("=" * 55)
    
    for domain in domains:
        try:
            # Resolves the domain name to an IP address
            ip_address = socket.gethostbyname(domain)
            print(f"Domain: {domain:<18} -> Resolved IP: {ip_address}")
        except socket.gaierror:
            print(f"❌ Could not resolve DNS for {domain}")

if __name__ == "__main__":
    analyze_search_engine_dns()
