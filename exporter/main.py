
#!/usr/bin/env python3
"""
CMMC Level 2 AC Controls Assessment Demo
Educational Version for Aspire Cyber Podcast
Demonstrates automated evidence generation for Access Control requirements
"""

import pandas as pd # pyright: ignore[reportMissingModuleSource]
import numpy as np # pyright: ignore[reportMissingImports]
from datetime import datetime, timedelta
from pathlib import Path
import sys
import argparse
import fileinput
import sys
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side # pyright: ignore[reportMissingModuleSource]
from openpyxl.utils import get_column_letter # type: ignore

print("="*60)
print("🎯 CMMC LEVEL 2 AC CONTROLS ASSESSMENT DEMO")
print("📺 Aspire Cyber Podcast Educational Version")
print("="*60)

# Mock company configuration
MOCK_COMPANY = {
    "name": "TechDefense Solutions LLC",
    "type": "Defense Subcontractor",
    "employees": 250,
    "cui_users": 85,
    "environment": "Hybrid (GCP + On-premise)",
    "assessment_date": datetime.now().strftime("%Y-%m-%d")
}

# AC Controls configuration
AC_CONTROLS = {
    "AC.L2-3.1.1": {
        "name": "Limit System Access",
        "description": "Limit system access to authorized users, processes, and devices",
        "evidence_types": ["Access Matrix", "User List", "Access Reviews"],
        "test_method": "Review access control matrix and sample user permissions"
    },
    "AC.L2-3.1.3": {
        "name": "Control CUI Flow",
        "description": "Control the flow of CUI in accordance with approved authorizations",
        "evidence_types": ["Network Diagram", "DLP Policies", "VPC Config"],
        "test_method": "Review network segmentation and data flow controls"
    },
    "AC.L2-3.1.6": {
        "name": "Session Lock",
        "description": "Use session lock with pattern-hiding displays",
        "evidence_types": ["GPO Settings", "Workspace Policy", "Test Results"],
        "test_method": "Verify timeout settings and test sample workstations"
    },
    "AC.L2-3.1.7": {
        "name": "Prevent Identifier Reuse",
        "description": "Prevent reuse of identifiers for a defined period",
        "evidence_types": ["Identity Policy", "Archived Users", "Retention Logs"],
        "test_method": "Review identity lifecycle management and retention"
    },
    "AC.L2-3.1.12": {
        "name": "Monitor Remote Access",
        "description": "Monitor and control remote access sessions",
        "evidence_types": ["VPN Logs", "Session Recordings", "SIEM Alerts"],
        "test_method": "Review remote access logs and monitoring configuration"
    },
    "AC.L2-3.1.20": {
        "name": "Control External Connections",
        "description": "Control and monitor external system connections",
        "evidence_types": ["Connection Inventory", "Monitoring Dashboard", "Attestations"],
        "test_method": "Review external connections and continuous monitoring"
    }
}

def generate_ac_evidence():
    """Generate mock evidence for AC controls"""
    evidence = []
    
    # AC.L2-3.1.1 - System Access
    evidence.append({
        "control_id": "AC.L2-3.1.1",
        "control_name": AC_CONTROLS["AC.L2-3.1.1"]["name"],
        "status": "COMPLIANT",
        "implementation": "Role-based access control via Google Cloud Identity + Active Directory",
        "evidence": "Access matrix showing 85 users with CUI access, quarterly review completed",
        "test_result": "Verified 10 sample users - all properly provisioned",
        "last_tested": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # AC.L2-3.1.3 - CUI Flow Control
    evidence.append({
        "control_id": "AC.L2-3.1.3",
        "control_name": AC_CONTROLS["AC.L2-3.1.3"]["name"],
        "status": "COMPLIANT",
        "implementation": "CUI isolated in dedicated VPC with DLP policies",
        "evidence": "VPC flow logs show no unauthorized data movement in 30 days",
        "test_result": "Firewall rules validated, DLP blocking test successful",
        "last_tested": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # AC.L2-3.1.6 - Session Lock
    evidence.append({
        "control_id": "AC.L2-3.1.6",
        "control_name": AC_CONTROLS["AC.L2-3.1.6"]["name"],
        "status": "COMPLIANT",
        "implementation": "15-minute timeout enforced via GPO and Workspace policy",
        "evidence": "100% of 250 workstations have timeout configured",
        "test_result": "Tested 25 random workstations - all locked at 15 minutes",
        "last_tested": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # AC.L2-3.1.7 - Identifier Reuse
    evidence.append({
        "control_id": "AC.L2-3.1.7",
        "control_name": AC_CONTROLS["AC.L2-3.1.7"]["name"],
        "status": "COMPLIANT",
        "implementation": "2-year minimum retention for all user identifiers",
        "evidence": "347 archived identifiers, none reused since policy implementation",
        "test_result": "Verified naming convention prevents collisions",
        "last_tested": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # AC.L2-3.1.12 - Remote Access Monitoring
    evidence.append({
        "control_id": "AC.L2-3.1.12",
        "control_name": AC_CONTROLS["AC.L2-3.1.12"]["name"],
        "status": "COMPLIANT",
        "implementation": "All remote access through VPN with MFA, sessions recorded",
        "evidence": "127 remote sessions in last 30 days, all logged and monitored",
        "test_result": "SIEM alerts working, demonstrated anomaly detection",
        "last_tested": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # AC.L2-3.1.20 - External Connections (with finding)
    evidence.append({
        "control_id": "AC.L2-3.1.20",
        "control_name": AC_CONTROLS["AC.L2-3.1.20"]["name"],
        "status": "PARTIALLY_COMPLIANT",
        "implementation": "Continuous monitoring of 12 external connections",
        "evidence": "Real-time dashboard, automated alerts at 30/7/0 days for attestations",
        "test_result": "2 vendor attestations expired - access auto-restricted to read-only",
        "last_tested": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "finding": "Vendor attestations expired for VEN-003 and VEN-007",
        "remediation": "Updated attestations expected by month-end"
    })
    
    return pd.DataFrame(evidence)

def generate_continuous_monitoring_data():
    """Generate continuous monitoring evidence for AC.L2-3.1.20"""
    connections = []
    
    # Mock external connections with monitoring data
    vendors = [
        ("VEN-001", "Raytheon", "Valid", "2024-12-15"),
        ("VEN-002", "Lockheed", "Valid", "2024-11-30"),
        ("VEN-003", "Northrop", "EXPIRED", "2024-08-30"),
        ("VEN-004", "Boeing", "Valid", "2025-01-15"),
        ("VEN-007", "L3Harris", "EXPIRED", "2024-08-28")
    ]
    
    for ven_id, name, status, expiry in vendors:
        connections.append({
            "connection_id": ven_id,
            "vendor_name": name,
            "connection_type": "VPN",
            "attestation_status": status,
            "expiry_date": expiry,
            "last_activity": (datetime.now() - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
            "data_transferred_24h": f"{np.random.randint(50, 500)}MB", # pyright: ignore[reportUndefinedVariable]
            "risk_score": "HIGH" if status == "EXPIRED" else "LOW",
            "access_level": "Read-Only" if status == "EXPIRED" else "Full",
            "monitoring_status": "Active",
            "alerts_sent": "Yes" if status == "EXPIRED" else "No"
        })
    
    return pd.DataFrame(connections)

def generate_assessment_summary(evidence_df):
    """Generate executive summary of assessment"""
    total = len(evidence_df)
    compliant = len(evidence_df[evidence_df['status'] == 'COMPLIANT'])
    partial = len(evidence_df[evidence_df['status'] == 'PARTIALLY_COMPLIANT'])
    
    summary = {
        'Assessment Date': [MOCK_COMPANY['assessment_date']],
        'Company': [MOCK_COMPANY['name']],
        'Total AC Controls': [total],
        'Fully Compliant': [compliant],
        'Partially Compliant': [partial],
        'Non-Compliant': [0],
        'Compliance Rate': [f"{(compliant/total)*100:.1f}%"],
        'Critical Findings': [partial]
    }
    
    return pd.DataFrame(summary)

def create_excel_report(output_file):
    """Generate comprehensive Excel report"""
    
    # Generate all data
    evidence = generate_ac_evidence()
    monitoring = generate_continuous_monitoring_data()
    summary = generate_assessment_summary(evidence)
    
    # Create Excel writer
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        
        # Executive Summary
        summary.to_excel(writer, sheet_name='Executive_Summary', index=False)
        
        # AC Controls Evidence
        evidence.to_excel(writer, sheet_name='AC_Controls_Evidence', index=False)
        
        # Continuous Monitoring (AC.L2-3.1.20)
        monitoring.to_excel(writer, sheet_name='External_Monitoring', index=False)
        
        # Apply formatting
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            
            # Header formatting
            header_fill = PatternFill(start_color='366092', end_color='366092', fill_type='solid')
            header_font = Font(color='FFFFFF', bold=True)
            
            for col in range(1, worksheet.max_column + 1):
                cell = worksheet.cell(row=1, column=col)
                cell.fill = header_fill
                cell.font = header_font
                cell.alignment = Alignment(horizontal='center', vertical='center')
            
            # Auto-fit columns
            for column_cells in worksheet.columns:
                length = max(len(str(cell.value or '')) for cell in column_cells)
                worksheet.column_dimensions[column_cells[0].column_letter].width = min(length + 2, 50)
            
            # Color-code status in evidence sheet
            if sheet_name == 'AC_Controls_Evidence':
                status_col = 3  # Status column
                for row in range(2, len(evidence) + 2):
                    status_cell = worksheet.cell(row=row, column=status_col)
                    if status_cell.value == 'COMPLIANT':
                        status_cell.fill = PatternFill(start_color='90EE90', end_color='90EE90', fill_type='solid')
                    elif status_cell.value == 'PARTIALLY_COMPLIANT':
                        status_cell.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    
    return output_file

def main():
    """Main execution"""
    parser = argparse.ArgumentParser(description='CMMC AC Controls Assessment Demo')
    parser.add_argument('--assessment', default='AC_CONTROLS', help='Assessment type')
    args = parser.parse_args()
    
    print(f"\n📋 Generating assessment for: {MOCK_COMPANY['name']}")
    print(f"👥 Employees: {MOCK_COMPANY['employees']} ({MOCK_COMPANY['cui_users']} with CUI access)")
    print(f"🔒 Focus: CMMC Level 2 Access Control Requirements\n")
    
    # Generate report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = Path(f"output/cmmc_ac_assessment_{timestamp}.xlsx")
    output_file.parent.mkdir(exist_ok=True)
    
    print("⚙️  Collecting evidence from mock systems...")
    print("   ✓ Access control matrix")
    print("   ✓ Session policies")
    print("   ✓ Remote access logs")
    print("   ✓ External connection monitoring")
    
    report = create_excel_report(output_file)
    
    print(f"\n✅ Assessment complete!")
    print(f"📁 Report generated: {output_file}")
    print("\n📊 Results Summary:")
    print("   • 5 of 6 AC controls FULLY COMPLIANT")
    print("   • 1 control PARTIALLY COMPLIANT (AC.L2-3.1.20)")
    print("   • Finding: 2 vendor attestations expired (auto-restricted)")
    print("\n" + "="*60)
    print("This educational demo shows automated evidence generation.")
    print("For production use, implement real API integrations.")
    print("="*60)

if __name__ == "__main__":
    main()

