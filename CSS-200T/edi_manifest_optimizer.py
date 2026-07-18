import sys

def optimize_edi_payload():
    print("==========================================================")
    print("       DATA SYSTEMS: EDI Manifest Transmission Analyzer   ")
    print("==========================================================\n")
    print("💡 Purpose: Validates electronic transaction document size")
    print("   boundaries to prevent server timeouts in legacy WMS.")
    print("==========================================================\n")

    try:
        # Ingesting raw document size context
        raw_input = input("📥 Enter electronic shipping manifest payload size (In Bytes): ").strip()
        if not raw_input.isdigit():
            raise ValueError
            
        bytes_size = int(raw_input)
        
        # 1. HARDWARE STORAGE SCALE CONVERSIONS
        bits_size = bytes_size * 8
        kb_size = bytes_size / 1024
        mb_size = kb_size / 1024

        # 2. LEGACY SYSTEM OVERHEAD VERIFICATION MATRIX
        # Real-world constraint: Many older AS400 mainframe EDI routers reject payloads over 2 MB
        if mb_size > 2.0:
            transmission_status = "❌ BLOCKED: Payload exceeds legacy 2MB server transfer threshold."
            optimization_action = "🛠️ ACTION REQUIRED: Fragment file into separate batches."
        else:
            transmission_status = "✅ APPROVED: Payload falls safely within transmission profiles."
            optimization_action = "🚀 READY: Safe to enqueue to carrier routing network pipeline."

        # 3. DISPLAY AUTOMATION BREAKDOWN
        print("\n=========================================================")
        print("             📑 TRANSMISSION INTEGRITY AUDIT             ")
        print("=========================================================")
        print(f"  🔢 Digital Scale (Bits) : {bits_size:,} bits")
        print(f"  📦 Base Footprint (Bytes): {bytes_size:,} B")
        print(f"  📊 Compressed Data (KB)  : {kb_size:.2f} KB")
        print(f"  💾 Master Profile (MB)   : {mb_size:.2f} MB")
        print("---------------------------------------------------------")
        print(f"  📢 Pipeline Strategy     : {transmission_status}")
        print(f"  🔧 Recommended Action    : {optimization_action}")
        print("=========================================================")

    except ValueError:
        print("\n❌ Format Error: System processing failed. Size inputs must be positive numbers.")

if __name__ == "__main__":
    optimize_edi_payload()
