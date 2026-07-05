import java.time.LocalDateTime;
import java.util.ArrayList;

// ==============================================================================
// ENTERPRISE DATA OBJECT ENCAPSULATION BLUEPRINT
// ==============================================================================
// WHY IT IS HERE: 
// This class models a single physical Order tracking node. By marking the internal 
// variables as 'private' (Encapsulation), we ensure that external scripts cannot 
// bypass warehouse protocols or change an order status arbitrarily from the outside.
// All data adjustments must go through verified, public class methods.
// ==============================================================================
class Order {
    private String orderId;
    private String destinationZip;
    private String status;
    private LocalDateTime statusUpdatedAt;

    // WHAT YOU ARE SEEING: Class Constructor Engine
    // HOW IT OPERATES: Instantiates and initializes a new unique inbound order asset.
    public Order(String orderId, String destinationZip) {
        this.orderId = orderId;
        
        // WHAT YOU ARE SEEING: Data Sanitization & Defensive Programming Layer.
        // HOW IT OPERATES: Uses Regular Expressions to guarantee the ZIP code is exactly 5 digits.
        // If data fails audit rules, the system defaults to a safe fallback hold state.
        if (destinationZip != null && destinationZip.matches("\\d{5}")) {
            this.destinationZip = destinationZip;
        } else {
            this.destinationZip = "UNKNOWN-HOLD"; 
            System.out.println("⚠️ WARNING: Order " + orderId + " placed on operational hold.");
        }
        
        this.status = "RECEIVED"; // Every physical entity begins lifecycle at the loading dock
        this.statusUpdatedAt = LocalDateTime.now();
    }

    // WHAT YOU ARE SEEING: State Machine Lifecycle Business Logic.
    // WHY IT'S HERE: In logistics, out-of-order statuses ruin database integrity.
    // This logic creates a strict "Sequence Enforcer" protecting workflow progression.
    public void advanceStatus(String nextStatus) {
        String targeted = nextStatus.toUpperCase();
        
        // HOW IT OPERATES: Condition evaluation preventing procedural state jumping.
        // An order cannot jump directly to "SHIPPED" without clearing inventory routing stages.
        if (this.status.equals("RECEIVED") && !targeted.equals("PICKED")) {
            System.out.println("❌ ERROR: Order " + orderId + " must go through 'PICKED' routing protocols first.");
            return;
        }
        
        this.status = targeted;
        this.statusUpdatedAt = LocalDateTime.now();
        System.out.println("🔄 Order " + orderId + " tracked status updated to: " + this.status);
    }

    // WHAT YOU ARE SEEING: Manifest Console Output Interface.
    public void displayManifest() {
        System.out.println("📦 Order ID: " + orderId + " | Status: " + status + " | Last Move: " + statusUpdatedAt);
    }
}

// ==============================================================================
// AUTOMATED FULFILLMENT OPERATIONAL EXECUTION ENGINE
// ==============================================================================
// WHY IT IS HERE: 
// This acts as the centralized control script or runtime dispatcher. It isolates 
// collection structures and looping operations entirely outside of individual assets, 
// maintaining a strict "Separation of Concerns" (SoC) design across files.
// ==============================================================================
public class FulfillmentTracker {
    public static void main(String[] args) {
        
        // WHAT YOU ARE SEEING: Strongly Typed Collection Instantiation.
        // HOW IT OPERATES: Reserves dynamic, resizable heap memory spaces specifically 
        // to manage and catalog incoming 'Order' objects sequentially.
        ArrayList<Order> warehouseFloor = new ArrayList<>();
        
        // WHAT YOU ARE SEEING: Entity Ingestion Layer.
        warehouseFloor.add(new Order("ORD-001", "75098")); // Inbound Wylie, TX Node
        warehouseFloor.add(new Order("ORD-002", "BAD-ZIP")); // Inbound Data Error Simulation
        
        System.out.println("\n--- Processing Active Warehouse Floor Manifest ---");
        
        // WHAT YOU ARE SEEING: Iteration Dispatch Workflow.
        // HOW IT OPERATES: Loops sequentially across all cached operational arrays, 
        // passing standard instructions down into individual object processing slots.
        for (Order order : warehouseFloor) {
            order.advanceStatus("PICKED"); // Request lifecycle state transition
            order.displayManifest();      // Output updated state variables to terminal
            System.out.println("----------------------------------------------");
        }
    }
}
