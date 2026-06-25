public class TempConverter {

    // Method demonstrating functional arithmetic return values
    public static double fahrenheitToCelsius(double fahrenheit) {
        return (fahrenheit - 32) * 5 / 9;
    }

    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("🌡️ CSS-200T: COMPUTATIONAL CORE METRIC CONVERTER");
        System.out.println("==================================================\n");

        // Array of dynamic test inputs (Fahrenheit temperatures)
        double[] fahrenheitTemps = {32.0, 72.5, 98.6, 212.0, 0.0};

        System.out.printf("%-15s | %-15s%n", "Fahrenheit", "Celsius");
        System.out.println("-----------------------------------");

        for (double f : fahrenheitTemps) {
            double c = fahrenheitToCelsius(f);
            // Formats output to exactly 2 decimal places for data consistency
            System.out.printf("%-15.1f | %-15.2f%n", f, c);
        }

        System.out.println("\n==================================================");
    }
}
