import socket

def analyze_search_engine_dns():
    # 🌍 WHAT YOU ARE SEEING: 
    # This list contains the domain names used by major search engines and their automated web crawlers.
    # Before a search engine can crawl, index, or display a website, it must first interact with these domains.
    domains = ["googlebot.com", "bing.com", "duckduckgo.com"]
    
    print("🌐 IT Student Network Analysis: Search Engines & DNS")
    print("=" * 55)
    
    for domain in domains:
        try:
            # ⚙️ HOW IT WORKS:
            # The socket.gethostbyname() function acts exactly like an operating system's DNS lookup.
            # It queries a DNS nameserver to translate the human-readable domain into a machine-readable IP address.
            ip_address = socket.gethostbyname(domain)
            print(f"Domain: {domain:<18} -> Resolved IP: {ip_address}")
            
        except socket.gaierror:
            # ⚠️ WHY IT MATTERS (TROUBLESHOOTING):
            # If a lookup fails, it simulates a network outage or a configuration error.
            # For IT students, understanding DNS failures is key because if a search bot cannot resolve 
            # a domain's IP, the entire website effectively disappears from the internet search index.
            print(f"❌ Could not resolve DNS for {domain}")

# 💡 WHY THIS IS HERE (THE "WHY" FOR IT STUDENTS):
# This script bridges the gap between internet infrastructure (DNS) and user-facing applications (Search Engines).
# Search engines handle billions of automated requests daily. IT infrastructure students must master 
# DNS because web crawler efficiency, global load balancing, and network availability all rely entirely 
# on how fast and securely these IP addresses can be resolved.
if __name__ == "__main__":
    analyze_search_engine_dns()
