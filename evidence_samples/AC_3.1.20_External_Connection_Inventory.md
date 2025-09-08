# EXTERNAL CONNECTION INVENTORY & MONITORING
## Live Dashboard: https://soc.techdefense.local/external-connections
## Last Updated: 2024-09-05 14:00:00 (Auto-refreshes every 5 minutes)

### Connection Registry

| ID | Vendor | Type | Purpose | CUI | Attestation | Expires | Status | Monitor |
|----|--------|------|---------|-----|-------------|---------|--------|---------|
| VEN-001 | Raytheon | VPN | Design specs | Yes | SOC2 Type II | 2024-12-15 | ✅ ACTIVE | 24/7 |
| VEN-002 | Lockheed | API | Parts catalog | No | ISO 27001 | 2024-11-30 | ✅ ACTIVE | 24/7 |
| VEN-003 | Northrop | VPN | Joint project | Yes | SOC2 Type II | 2024-08-30 | ⚠️ EXPIRED | Restricted |
| VEN-004 | Boeing | SFTP | Doc exchange | Yes | FedRAMP Mod | 2025-01-15 | ✅ ACTIVE | 24/7 |
| VEN-005 | General Dynamics | API | Supply chain | No | ISO 27001 | 2024-10-31 | ⚠️ 56 DAYS | 24/7 |
| VEN-006 | BAE Systems | VPN | Testing lab | Yes | CMMC L2 | 2024-12-01 | ✅ ACTIVE | 24/7 |
| VEN-007 | L3Harris | VPN | Research | Yes | CMMC L2 | 2024-08-28 | ⚠️ EXPIRED | Restricted |
| VEN-008 | Textron | API | Inventory | No | SOC2 Type I | 2025-02-28 | ✅ ACTIVE | 24/7 |
| VEN-009 | Honeywell | SFTP | Sensors | Yes | ISO 27001 | 2024-11-15 | ✅ ACTIVE | 24/7 |
| VEN-010 | SAIC | VPN | Analytics | No | FedRAMP Low | 2024-10-15 | ⚠️ 40 DAYS | 24/7 |
| VEN-011 | CACI | API | Intel feeds | Yes | SOC2 Type II | 2025-01-31 | ✅ ACTIVE | 24/7 |
| VEN-012 | Leidos | VPN | Joint dev | Yes | FedRAMP High | 2025-03-31 | ✅ ACTIVE | 24/7 |

### Continuous Monitoring Configuration

```yaml
monitoring:
  frequency: "5 minutes"
  checks:
    - certificate_validation
    - connection_health
    - data_volume_anomaly
    - attestation_expiry
  
  alerts:
    90_days: "Email to vendor + security team"
    30_days: "Daily email reminders"
    7_days: "Escalate to CISO"
    0_days: "Auto-restrict to read-only"
    
  automated_actions:
    on_expiry: "Restrict access to read-only"
    on_suspicious: "Alert SOC + log for review"
    on_certificate_fail: "Block connection + alert"
Recent Automated Actions
TimestampConnectionEventAction Taken2024-08-30 00:00:01VEN-003Attestation expiredAccess restricted to read-only2024-08-28 00:00:01VEN-007Attestation expiredAccess restricted to read-only2024-08-23 09:00:00VEN-0037-day warning sentEmail to vendor + CISO2024-08-21 09:00:00VEN-0077-day warning sentEmail to vendor + CISO2024-08-01 09:00:00VEN-00590-day warning sentInitial notification2024-08-01 09:00:00VEN-01090-day warning sentInitial notification
Connection Monitoring Metrics (Last 30 Days)

Total Connections Monitored: 12
Active Connections: 8
Restricted/Expired: 2
Expiring Soon (< 60 days): 2
Alerts Generated: 47
Auto-Remediations: 2
Average Response Time: < 5 minutes
Monitoring Uptime: 99.97%

Evidence of Continuous Monitoring
{
  "last_scan": "2024-09-05T14:00:00Z",
  "next_scan": "2024-09-05T14:05:00Z",
  "automated_checks": {
    "certificate_validation": "PASS",
    "connection_health": "PASS",
    "attestation_status": "2 EXPIRED, 2 WARNING",
    "anomaly_detection": "NONE"
  },
  "actions_taken": [
    {
      "vendor": "VEN-003",
      "action": "restrict_access",
      "reason": "attestation_expired",
      "timestamp": "2024-08-30T00:00:01Z"
    },
    {
      "vendor": "VEN-007",
      "action": "restrict_access",
      "reason": "attestation_expired",
      "timestamp": "2024-08-28T00:00:01Z"
    }
  ]
}
System: Automated GRC Platform v2.3
Human Review: Weekly by Security Team
Next Manual Audit: 2024-09-15
POC: Security Operations Center (soc@techdefense.com)
