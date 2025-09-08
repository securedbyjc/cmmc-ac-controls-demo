# SCREENSHOT: External Connection Monitoring Dashboard
## Captured: 2024-08-30 00:05:00 UTC (5 minutes after auto-restriction)
## System: TechDefense SOC Dashboard v3.2

### Real-Time Status Panel

**CONNECTION: VEN-003 - Northrop Grumman**

| Field | Value |
|-------|-------|
| **Status** | ⚠️ RESTRICTED (Changed from ACTIVE at 00:00:01) |
| **CUI Access** | ❌ BLOCKED |
| **General Access** | ✅ Read-Only |
| **Connection Type** | Site-to-Site VPN |
| **Data Transfer (24h)** | 0 MB (blocked at 00:00) |
| **Last Valid Activity** | 2024-08-29 23:47:33 |

### Automated Timeline

| Timestamp | Event | Action |
|-----------|-------|--------|
| 2024-06-01 09:00 | 90-day warning | Email sent to vendor and security team |
| 2024-07-31 09:00 | 30-day warning | Email sent with escalation to management |
| 2024-08-23 09:00 | 7-day critical warning | CISO notified, vendor contacted directly |
| 2024-08-30 00:00 | Attestation expired | System detected expiration |
| **2024-08-30 00:00:01** | **AUTO-RESTRICTED** | **Access automatically limited to read-only** |

### Automated Actions Completed

- ✅ Firewall rules updated (1.2 seconds)
- ✅ CUI access revoked (0.8 seconds)
- ✅ Vendor notification sent
- ✅ Incident logged: INC-2024-0830-001
- ✅ Compliance team alerted
- ✅ Evidence package generated

### System Alert

> **SEVERITY: HIGH**  
> **TIME: 2024-08-30 00:00:01.234**
> 
> External connection VEN-003 has been automatically restricted due to expired security attestation. This action was taken per policy AC-POL-3.1.20 without human intervention.
> 
> **Required Action:** Vendor must provide updated SOC 2 Type II attestation to restore full access.

### Connection Health Metrics

- **Uptime before restriction:** 99.98%
- **Failed connection attempts post-restriction:** 3 (all blocked)
- **Successful read-only connections:** 12
- **Time to auto-restrict:** 1.456 seconds
- **Human intervention required:** None

---

*Screenshot captured from TechDefense Security Operations Center*  
*Automated restriction executed without manual intervention*  
*Evidence preserved per AU.L2-3.3.1 requirements*
