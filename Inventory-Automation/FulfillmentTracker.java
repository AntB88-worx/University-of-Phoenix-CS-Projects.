import java.time.LocalDateTime;
import java.util.ArrayList;

class Order {
    private String orderId;
    private String destinationZip;
    private String status;
    private LocalDateTime statusUpdatedAt;

    public Order(String orderId, String destinationZip) {
        this.orderId = orderId;
        if (destinationZip != null && destinationZip.matches("\\d{5}")) {
            this.destinationZip = destinationZip;
        } else {
            this.destinationZip = "UNKNOWN-HOLD";
            System.out.println("⚠️ WARNING: Order " + orderId + " placed on hold.");
        }
        this.status = "RECEIVED";
        this.statusUpdatedAt = LocalDateTime.now();
    }

    public void advanceStatus(String nextStatus) {
        String targeted = nextStatus.toUpperCase();
        if (this.status.equals("RECEIVED") && !targeted.equals("PICKED")) {
            System.out.println("❌ ERROR: Order " + orderId + " must be PICKED first.");
            return;
        }
        this.status = targeted;
        this.statusUpdatedAt = LocalDateTime.now();
        System.out.println("🔄 Order " + orderId + " updated to: " + this.status);
    }

    public void displayManifest() {
        System.out.println("📦 Order ID: " + orderId + " | Status: " + status);
    }
}

public class FulfillmentTracker {
    public static void main(String[] args) {
        ArrayList<Order> warehouseFloor = new ArrayList<>();
        warehouseFloor.add(new Order("ORD-001", "75098"));
        
        System.out.println("--- Processing Orders ---");
        for (Order order : warehouseFloor) {
            order.advanceStatus("PICKED");
            order.displayManifest();
        }
    }
}
