import java.time.LocalDateTime;
import java.util.ArrayList;

/**
 * REPRESENTATION OF A PHYSICAL WAREHOUSE ASSET
 * This class encapsulates individual shipment details and movement rules.
 */
class Order {
    private String orderId;
    private String destinationZip;
    private String status;
    private LocalDateTime statusUpdatedAt;

    // CONSTRUCTOR: Instantiates and initializes a new inbound order
    public Order(String orderId, String destinationZip) {
        this.orderId = orderId;
        
        // STEP 1: Verify data integrity (Ensures the ZIP code is exactly 5 numbers)
        if (destinationZip != null && destinationZip.matches("\\d{5}")) {
            this.destinationZip = destinationZip;
        } else {
            this.destinationZip = "UNKNOWN-HOLD"; // Puts bad data on hold immediately
            System.out.println("⚠️ WARNING: Order " + orderId + " placed on hold.");
        }
        
        this.status = "RECEIVED"; // All orders start at the loading dock
        this.statusUpdatedAt = LocalDateTime.now();
    }

    // BUSINESS LOGIC: Safely advances the order through milestones
    public void advanceStatus(String nextStatus) {
        String targeted = nextStatus.toUpperCase();
        
        // STEP 2: Sequence Enforcer (Cannot skip straight to packed/shipped)
        if (this.status.equals("RECEIVED") && !targeted.equals("PICKED")) {
            System.out.println("❌ ERROR: Order " + orderId + " must be PICKED first.");
            return;
        }
        
        this.status = targeted;
        this.statusUpdatedAt = LocalDateTime.now();
        System.out.println("🔄 Order " + orderId + " updated to: " + this.status);
    }

    // MANIFEST DISPLAY: Prints the current asset status to the warehouse console
    public void displayManifest() {
        System.out.println("📦 Order ID: " + orderId + " | Status: " + status);
    }
}

/**
 * MAIN WORKFLOW ENGINE
 * Run this class to execute the automated fulfillment tracking pipeline.
 */
public class FulfillmentTracker {
    public static void main(String[] args) {
        // STEP 3: Setup a dynamic collection to hold our incoming manifest batch
        ArrayList<Order> warehouseFloor = new ArrayList<>();
        
        // STEP 4: Ingest and create orders on the warehouse floor
        warehouseFloor.add(new Order("ORD-001", "75098")); // Wylie, TX order
        
        System.out.println("--- Processing Orders ---");
        
        // STEP 5: Loop through our collection and execute active floor movements
        for (Order order : warehouseFloor) {
            order.advanceStatus("PICKED"); // Move to picked status
            order.displayManifest();      // Print out the updated state
        }
    }
}

