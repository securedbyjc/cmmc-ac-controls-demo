\# CMMC Level 2 Access Control Assessment Demo



<div align="center">



\[!\[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

\[!\[Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

\[!\[CMMC](https://img.shields.io/badge/CMMC-Level%202-green.svg)](https://www.acq.osd.mil/cmmc/)



\*\*Transform CMMC Assessment Evidence into Audit-Ready Reports in Seconds\*\*



\[\*\*Quick Start\*\*](#-quick-start) • \[\*\*Features\*\*](#-features) • \[\*\*Demo\*\*](#-live-demo) • \[\*\*Why This Matters\*\*](#-why-this-matters) • \[\*\*Contact\*\*](#-contact)



</div>



---



\## 🎯 The Challenge



\*\*Defense contractors spend countless hours gathering evidence for CMMC assessments.\*\*



Every CMMC Level 2 assessment requires the same painful process:

\- Manually collecting evidence from multiple systems

\- Documenting 110+ practices across 14 domains

\- Formatting evidence for assessor review

\- Mapping technical controls to CMMC requirements

\- Scrambling to fill gaps discovered during assessment



\*\*What if evidence collection could be automated and continuous?\*\*



\## 💡 The Solution



This educational demo shows how to automatically generate CMMC Level 2 Access Control evidence from your existing security tools, creating assessor-ready documentation that CCA/CCP assessors expect. No more evidence scrambles. No more failed assessments.



\## 🚀 Quick Start



```bash

\# Clone the repository

git clone https://github.com/securedbyjc/cmmc-ac-controls-demo.git

cd cmmc-ac-controls-demo



\# Install dependencies

pip install -r requirements.txt



\# Run the assessment demo

python exporter/main.py --assessment AC\_CONTROLS



\# Output appears in timestamped folder

\# output/cmmc\_ac\_assessment\_20240905\_143022.xlsx



That's it! In under 10 seconds, you have evidence for all 6 critical AC controls ready for your assessor.



✨ Features

🔒 Six Critical AC Controls Demonstrated



AC.L2-3.1.1 - Limit system access to authorized users

AC.L2-3.1.3 - Control the flow of CUI

AC.L2-3.1.6 - Use session lock with pattern-hiding displays

AC.L2-3.1.7 - Prevent reuse of identifiers

AC.L2-3.1.12 - Monitor and control remote access

AC.L2-3.1.20 - Verify and control external connections



📊 Continuous Monitoring Capabilities

Real-time external connection monitoring, automated compliance verification, proactive alert generation, and access restriction on non-compliance.

📁 Evidence Package Generation



Assessor-ready Excel workbooks

Policy and procedure artifacts

Technical configuration screenshots

Compliance status dashboards

Gap analysis with remediation tracking



🎨 Professional Assessment Output



Color-coded compliance status (Compliant=Green, Partial=Yellow, Non-Compliant=Red)

Evidence mapping to specific CMMC practices

Test procedure documentation showing validation methods

Continuous monitoring dashboards for AC.L2-3.1.20

Executive summary with compliance metrics



🎬 Live Demo

Before: Manual Evidence Collection

Hours spent gathering:

\- Access control matrices from Active Directory

\- VPN logs from multiple systems  

\- Session timeout settings from GPOs

\- External connection inventories

\- Security attestations from vendors



\### After: Automated Assessment Package



| Control | Status | Evidence | Test Result | Finding |

|---------|--------|----------|-------------|---------|

| AC.L2-3.1.1 | ✅ COMPLIANT | Access Matrix, User Reviews | 10 users sampled - all correct | None |

| AC.L2-3.1.3 | ✅ COMPLIANT | VPC Config, DLP Policies | CUI properly segmented | None |

| AC.L2-3.1.6 | ✅ COMPLIANT | GPO Settings, Test Results | 100% workstations configured | None |

| AC.L2-3.1.20 | ⚠️ PARTIAL | Connection Inventory, Monitoring | Continuous monitoring active | 2 attestations expired |



📈 Why This Matters

For Defense Contractors



Assessment readiness maintained continuously

Evidence gaps identified before assessors arrive

Remediation tracking for findings

Cost reduction from shorter assessment periods



For Virtual GRC Consultants



Accelerated assessments with pre-generated evidence

Consistent documentation across clients

Continuous monitoring between assessments

Professional deliverables that impress assessors



For the Defense Industrial Base



Strengthens supply chain security posture

Reduces barriers for small businesses

Standardizes evidence collection practices

Accelerates CMMC adoption



🏗️ Architecture

graph LR

&nbsp;   A\[Security Tools] --> B\[Evidence Collector]

&nbsp;   B --> C\[CMMC Mapper]

&nbsp;   C --> D\[Assessment Generator]

&nbsp;   D --> E\[Excel Package]

&nbsp;   

&nbsp;   F\[Continuous Monitor] --> G\[Real-time Alerts]

&nbsp;   G --> H\[Auto-remediation]

<details>

<summary>📁 Project Structure</summary>

cmmc-ac-controls-demo/

├── exporter/

│   ├── main.py              # Assessment engine

│   └── requirements.txt     # Python dependencies

├── mock\_data/

│   ├── access\_matrix.json   # User access data

│   ├── vpc\_config.json      # Network configuration

│   └── monitoring\_data.json # Continuous monitoring

├── evidence\_samples/        # Example artifacts

│   ├── policies/

│   └── screenshots/

├── output/                  # Generated assessments

└── README.md

</details>

🎓 Educational Purpose

This is a demonstration project created for the Aspire Cyber Podcast to show:



How CMMC evidence can be automated

Continuous monitoring for compliance

Professional assessment documentation

Integration patterns with security tools



Note: This educational version includes simplified controls and mock data. Production implementations require all 110 practices and real system integrations.

\## 🚀 Taking This to Production



Ready for comprehensive CMMC automation? The production version includes:



\### Technical Controls (What We CAN Automate):

\- ✅ ~60-70 technical practices across domains:

&nbsp; - Access Control (AC) - System configurations

&nbsp; - Audit \& Accountability (AU) - Log collection

&nbsp; - Configuration Management (CM) - Baseline monitoring

&nbsp; - Identification \& Authentication (IA) - MFA status

&nbsp; - System \& Communications Protection (SC) - Encryption verification

&nbsp; - System \& Information Integrity (SI) - Vulnerability scanning

&nbsp; - Incident Response (IR) - Alert correlation

&nbsp; 

\### What Requires Human Process:

\- ❌ Personnel Security (PS) - Background checks, training records

\- ❌ Physical Protection (PE) - Facility controls

\- ❌ Awareness \& Training (AT) - Training completion records

\- ❌ Risk Assessment (RA) - Risk analysis documentation

\- ❌ Security Assessment (CA) - Assessment plans

\- ❌ Maintenance (MA) - Maintenance logs

\- ❌ Media Protection (MP) - Media handling procedures



\### Production Capabilities:

\- ✅ Real-time API integration with security tools

\- ✅ Continuous monitoring of technical controls

\- ✅ Automated evidence refresh

\- ✅ Integration with GRC platforms for non-technical tracking

\- ✅ Dashboard showing technical vs. administrative control coverage

\- ✅ Export to assessment tools (Prevail, eMASS)



🤝 Contributing



We welcome contributions from the CMMC community:



Additional CMMC practices

Integration with new security tools

Enhanced monitoring capabilities

Assessment report templates



📚 Resources



CMMC Model Overview

NIST SP 800-171 Rev 2

CMMC Assessment Guides

Aspire Cyber Podcast

CPN - CMMC Professionals Network

👥 About the Demo Creator  

Jeffrey Collins, CSM® — Founder of \*\*Eagle Defense Systems\*\* and Virtual GRC Consultant specializing in CMMC readiness for defense contractors.  

As a \*\*Professional Member of the CMMC Professional Network (CPN)\*\*, Jeffrey receives specialized training on the \*\*Prevail assessment platform\*\* and hands-on instruction across major GovCloud environments, including \*\*AWS GovCloud (US)\*\* and \*\*Microsoft GCC High\*\*. This expertise enables him to support defense and government contractors in achieving and maintaining compliance with evolving cybersecurity standards.


🎬 Demo Context

Created for: Aspire Cyber Podcast - CMMC Level 2 Assessment Series

Mock Company: TechDefense Solutions LLC - 250 employees, defense subcontractor



📬 Contact

Ready to automate your CMMC assessment evidence?



Email: info@eagledefensesys.tech

Website: eagledefensesys.tech

LinkedIn: Jeffrey Collins

Podcast: Aspire Cyber



📜 License

This educational demonstration is released under the MIT License. See LICENSE file for details.

⚖️ Disclaimer

This is an educational demonstration tool created for the Aspire Cyber Podcast. It demonstrates concepts only and is not intended for production use without proper implementation of all 110 CMMC practices, real system integrations, and comprehensive testing. No warranty is provided, express or implied.



<div align="center">

Featured on Aspire Cyber Podcast | CMMC Community Resource | Open Source Education

Transforming CMMC compliance from a burden into continuous readiness

🌟 Star this repo if you find it helpful!

</div>

```


< temp: verify path -->

< temp: verify path -->
