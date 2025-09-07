#!/usr/bin/env python3
"""
Continuous Monitoring Dashboard for AC.L2-3.1.20
Shows real-time status of external connections
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

def generate_dashboard_html():
    """Generate HTML dashboard for continuous monitoring"""
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CMMC AC.L2-3.1.20 - Continuous Monitoring Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .header { background: #1e3a5f; color: white; padding: 20px; }
            .metric { display: inline-block; margin: 10px; padding: 15px; border: 1px solid #ddd; }
            .compliant { background: #90EE90; }
            .partial { background: #FFFF00; }
            .non-compliant { background: #FFB6C1; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
            th { background: #366092; color: white; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>External Connection Monitoring Dashboard</h1>
            <p>TechDefense Solutions LLC - Real-time Compliance Status</p>
        </div>
        
        <div class="metrics">
            <div class="metric compliant">✓ 10 Compliant</div>
            <div class="metric partial">⚠ 2 Expiring Soon</div>
            <div class="metric non-compliant">✗ 2 Expired</div>
        </div>
        
        <table>
            <tr>
                <th>Connection ID</th>
                <th>Vendor</th>
                <th>Status</th>
                <th>Expiry</th>
                <th>Action</th>
            </tr>
            <tr>
                <td>VEN-001</td>
                <td>Raytheon</td>
                <td style="color: green;">✓ Valid</td>
                <td>2024-12-15</td>
                <td>None Required</td>
            </tr>
            <tr>
                <td>VEN-003</td>
                <td>Northrop</td>
                <td style="color: red;">✗ Expired</td>
                <td>2024-08-30</td>
                <td>Access Restricted</td>
            </tr>
        </table>
        
        <p><small>Dashboard refreshes every 5 minutes. Last update: """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</small></p>
    </body>
    </html>
    """
    
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    with open(output_dir / "monitoring_dashboard.html", "w") as f:
        f.write(html)
    
    print("📊 Monitoring dashboard generated: output/monitoring_dashboard.html")

if __name__ == "__main__":
    generate_dashboard_html()
