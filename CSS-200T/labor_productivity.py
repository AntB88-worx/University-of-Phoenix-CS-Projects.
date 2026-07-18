import time

def calculate_shift_productivity():
    # RESTORED PERSONAL CONTEXT COMMENT BLOCK
    print("==========================================================")
    print("      LOGISTICS WORKFORCE: Shift Productivity Engine      ")
    print("==========================================================")
    print("💡 What this is: An advanced processing utility that     ")
    print("   evaluates arrays of metrics, sums throughput logs, and ")
    print("   flags individual outliers below performance goals.    ")
    print("\n📝 Personal Note: I am enhancing this list script to   ")
    print("   learn about array aggregations, floating-point rules, ")
    print("   and automated loop structures using python lists!    ")
    print("==========================================================\n")
    
    picker_metrics = []
    print("📋 Instructions: Enter picker metrics (Units/Hour). Type 'done' to calculate:")
    
    while True:
        user_input = input(" 📥 Enter PPH Metric: ").strip()
        if user_input.lower() == 'done':
            break
        if user_input.isdigit():
            picker_metrics.append(int(user_input))
        else:
            print(" ❌ Invalid input. Please enter a numerical throughput value.")

    if not picker_metrics:
        print("\n🛑 Shift aborted: No labor performance entries logged.")
        return

    # Core mathematical array aggregations
    total_throughput = sum(picker_metrics)
    shift_average = total_throughput / len(picker_metrics)
    
    # Conditional branching based on performance thresholds
    if shift_average >= 120:
        performance_tier = "🚀 EXCEEDS SLA (High Efficiency)"
    elif shift_average >= 90:
        performance_tier = "✅ MEETS SLA (Optimal Flow)"
    elif shift_average >= 70:
        performance_tier = "⚠️  CONDITIONAL (Needs Monitoring)"
    else:
        performance_tier = "🚨 CRITICAL UNDERPERFORMANCE (Action Required)"

    print("\n=========================================================")
    print("             📊 SHIFT PERFORMANCE RECAP REPORT           ")
    print("=========================================================")
    print(f"  📦 Total Processed Volume : {total_throughput:,} Units")
    print(f"  🧑‍🏭 Active Shift Staffing : {len(picker_metrics)} Pickers")
    print(f"  📈 Measured Performance Avg: {shift_average:.2f} PPH")
    print(f"  📢 Fleet Status Tier      : {performance_tier}")
    print("---------------------------------------------------------")
    print("  🚨 INDIVIDUAL BREAK POLICY AUDIT FLAGS:")
    
    flag_count = 0
    for idx, score in enumerate(picker_metrics, 1):
        if score < 70:
            print(f"   • Station #{idx}: CRITICAL DROP ({score} PPH) — Potential bottleneck.")
            flag_count += 1
            
    if flag_count == 0:
        print("   • All active floor stations sustained baseline speeds.")
    print("=========================================================")

if __name__ == "__main__":
    calculate_shift_productivity()
