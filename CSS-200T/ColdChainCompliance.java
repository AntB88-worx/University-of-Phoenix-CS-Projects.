import java.util.Date;

public class ColdChainCompliance {
    public static void main(String[] args) {
        System.out.println("==========================================================");
        System.out.println("      COLD CHAIN AUDIT: Reefers Thermal Compliance        ");
        System.out.println("==========================================================\n");

        // 1. DATA ARRAY: Raw Fahrenheit telemetry points recorded during a delivery route
        double[] fahrenheitLogs = {34.2, 38.5, 42.1, 31.8, 45.3, 35.0, 41.5};

        System.out.println("🔄 Executing conversion algorithms and mapping regulatory compliance thresholds...");
        System.out.println("\n=====================================================================");
        System.out.printf("  %-12s | %-15s | %-15s | %-15s \n", "SENSOR NODE", "RAW FAHRENHEIT", "CELSIUS METRIC", "RISK METADATA");
        System.out.println("=====================================================================");

        // 2. ITERATIVE ITERATION LOOP: Evaluates type consistency and applies equations
        for (int i = 0; i < fahrenheitLogs.length; i++) {
            double fahrenheit = fahrenheitLogs[i];
            
            // Core conversion functional formula
            double celsius = (fahrenheit - 32) * 5 / 9;
            
            // 3. REGULATORY COMPLIANCE MATRICES: FDA food/pharma storage restrictions (>40°F / >4.4°F is dangerous)
            String riskStatus;
            if (fahrenheit > 40.0) {
                riskStatus = "❌ TEMPERATURE BREACH";
            } else if (fahrenheit < 32.0) {
                riskStatus = "⚠️  FREEZE RISK";
            } else {
                riskStatus = "✅ SECURE STORAGE";
            }

            // Structured tabular layout printing out console metadata spacing
            System.out.printf("  Sensor #%02d    | %-15.2f | %-15.2f | %-15s \n", (i + 1), fahrenheit, celsius, riskStatus);
        }
        System.out.println("=====================================================================");
        System.out.println("🏁 Cold chain thermal inspection processing complete.");
    }
}

