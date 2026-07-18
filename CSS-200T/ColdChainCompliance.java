public class ColdChainCompliance {
    public static void main(String[] args) {
        // RESTORED ACADEMIC PURPOSE AND METADATA PRINT SHEETS
        System.out.println("==========================================================");
        System.out.println("      COLD CHAIN AUDIT: Reefers Thermal Compliance        ");
        System.out.println("==========================================================");
        System.out.println("💡 What this is: A Java tracking module utilizing static  ");
        System.out.println("   methods and structured matrices to evaluate arrays.    ");
        System.out.println("\n📝 Personal Note: I wrote this file to master precise   ");
        System.out.println("   primitive double casting and data alignment protocols  ");
        System.out.println("   across complex tabular console displays!               ");
        System.out.println("==========================================================\n");

        double[] fahrenheitLogs = {34.2, 38.5, 42.1, 31.8, 45.3, 35.0, 41.5};

        System.out.println("🔄 Processing data-type consistency arrays...");
        System.out.println("\n=====================================================================");
        System.out.printf("  %-12s | %-15s | %-15s | %-15s \n", "SENSOR NODE", "RAW FAHRENHEIT", "CELSIUS METRIC", "RISK METADATA");
        System.out.println("=====================================================================");

        // Functional processing looping structure
        for (int i = 0; i < fahrenheitLogs.length; i++) {
            double fahrenheit = fahrenheitLogs[i];
            
            // Formula equation tracking double variables
            double celsius = (fahrenheit - 32) * 5 / 9;
            
            String riskStatus;
            if (fahrenheit > 40.0) {
                riskStatus = "❌ TEMPERATURE BREACH";
            } else if (fahrenheit < 32.0) {
                riskStatus = "⚠️  FREEZE RISK";
            } else {
                riskStatus = "✅ SECURE STORAGE";
            }

            System.out.printf("  Sensor #%02d    | %-15.2f | %-15.2f | %-15s \n", (i + 1), fahrenheit, celsius, riskStatus);
        }
        System.out.println("=====================================================================");
    }
}
