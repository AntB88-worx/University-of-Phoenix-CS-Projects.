import java.time.LocalDateTime;

// Base Object showcasing encapsulation for operational assets
class Order {
    private String orderId;
    private String destinationZip;
    private String status;
    private LocalDateTime statusUpdatedAt;

    public Order(String orderId, String destinationZip) {
        this.orderId = orderId;
        this.destinationZip = destinationZip;
        this.status = "RECEIVED";
        this.statusUpdatedAt = LocalDateTime.now();
    }

    // Business rule mechanism to step through logistics milestones safely
    public void advanceStatus(String nextStatus) {
        this.status = nextStatus.toUpperCase();
        this.statusUpdatedAt = LocalDateTime.now();
        System.out.println("🔄 Order " + orderId + " updated to status: [" + this.status + "] at " + this.statusUpdatedAt);
    }

    public void displayManifest() {
        System.out.println("📦 Order ID: " + orderId + " | Dest: " + destinationZip + " | Status: " + status);
    }
}

public class FulfillmentTracker {
    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("🏭 WORKFLOW ENGINE: ORDER FULFILLMENT TRACKER");
        System.out.println("==================================================\n");

        // Instantiate inbound warehouse orders
        Order order1 = new Order("ORD-2026-A", "75098"); // Wylie, TX zip
        Order order2 = new Order("ORD-2026-B", "75201"); // Dallas, TX zip

        order1.displayManifest();
        order2.displayManifest();
        System.out.println();

        // Simulate active floor movements
        System.out.println("--- Executing Warehouse Movements ---");
        order1.advanceStatus("PICKED");
        order2.advanceStatus("PICKED");
        order1.advanceStatus("PACKED");
        order1.advanceStatus("SHIPPED");
        System.out.println();

        System.out.println("--- Final Manifest State ---");
        order1.displayManifest();
        order2.displayManifest();
        System.out.println("\n==================================================");
    }
}
