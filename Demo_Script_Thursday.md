# DEMO SCRIPT FOR AC.L2-3.1.20

## Opening Statement

"Let me demonstrate our continuous monitoring for external connections. As you can see in our inventory, we have 12 external connections, with 2 currently restricted due to expired attestations."

## Show the Evidence Chain

### 1. Show the Inventory (AC_3.1.20_External_Connection_Inventory.md)

"Here's our live inventory showing VEN-003 and VEN-007 with expired attestations"

### 2. Show the Dashboard "Screenshot"

"This is what our SOC sees when an attestation expires - the system automatically restricts access"

### 3. Show the Firewall Logs

"Here are the actual firewall logs showing the automatic rule change at exactly midnight when the attestation expired"

### 4. Show the Email Trail

"The system sent automated alerts at 90, 30, and 7 days. When the vendor didn't respond, access was automatically restricted"

### 5. Run the Python Tool

"Now let me show how our automated tool aggregates all this evidence for assessment"
[Run: python.exe exporter/main.py]

## Assessor Questions to Prepare For

Q: "How do I know the restriction actually happened?"
A: "Here's the firewall log showing the exact timestamp and rule change, plus the failed connection attempts after restriction"

Q: "What if a vendor needs emergency access?"
A: "We have a documented exception process requiring CISO approval with compensating controls"

Q: "How often does this monitoring run?"
A: "Every 5 minutes for connection health, daily for attestation status"
