def convert_bytes(byte_count):
    # Calculations based on foundational CS principles:
    # 1 Byte is equal to 8 Bits.
    # 1 Kilobyte (KB) is equal to 1,024 Bytes.
    # 1 Megabyte (MB) is equal to 1,024 Kilobytes.
    bits = byte_count * 8
    kilobytes = byte_count / 1024
    megabytes = kilobytes / 1024
    
    print(f"\n--- Data Conversion Results for {byte_count} Bytes ---")
    print(f"🔢 Bits: {bits:,} b (Calculated as Bytes x 8)")
    print(f"📁 Kilobytes: {kilobytes:.4f} KB (Calculated as Bytes / 1,024)")
    print(f"💿 Megabytes: {megabytes:.6f} MB (Calculated as KB / 1,024)")

if __name__ == "__main__":
    # Introductory message explaining the purpose and personal context of the script
    print("==========================================================")
    print("       CSS-200T: Bits & Bytes Data Storage Converter      ")
    print("==========================================================")
    print("💡 What this is: A utility to visualize how computers store")
    print("   and measure digital data sizes behind the scenes.")
    print("\n📝 Personal Note: I just learned about data sizes, bits,")
    print("   and bytes in class today and wanted to test the math")
    print("   out myself using Python logic!")
    print("==========================================================\n")
    
    try:
        user_input = int(input("Enter an amount of bytes to convert: "))
        if user_input < 0:
            print("❌ Please enter a positive number.")
        else:
            convert_bytes(user_input)
    except ValueError:
        print("❌ Invalid input. Please enter a whole number.")
