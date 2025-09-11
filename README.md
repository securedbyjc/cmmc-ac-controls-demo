# CMMC Level 2 AC Evidence Automation Demo

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![CMMC](https://img.shields.io/badge/CMMC-L2-green.svg)
![NIST 800-171](https://img.shields.io/badge/NIST-800--171-blue.svg)
![FedRAMP](https://img.shields.io/badge/FedRAMP-Reference-lightgrey.svg)

Transform CMMC L2 Access Control findings into **audit-ready Excel evidence** in seconds.

[**Quick Start**](#quick-start) • [**Features**](#features) • [**Demo**](#demo) • [**Why This Matters**](#why-this-matters) • [**Architecture**](#architecture) • [**Project Structure**](#project-structure) • [**Educational Purpose**](#educational-purpose) • [**Taking This to Production**](#taking-this-to-production) • [**Contributing**](#contributing) • [**Resources**](#resources) • [**About Eagle Defense Systems**](#about-eagle-defense-systems) • [**Contact**](#contact) • [**License**](#license) • [**Disclaimer**](#disclaimer)

---

## 🎯 The Challenge

GRC and security teams burn time on **data wrangling**, not outcomes. Common pain points:
- Exports from IdP, VPN, SIEM, and MDM tools
- Manual mapping to **CMMC L2 (NIST 800-171)** practices
- Copy/paste into Excel templates
- Formatting and hyperlinking artifacts
- Human errors and rework right before assessments

**What if this was automated?**

## 💡 The Solution

This educational demo turns **security signals + artifacts** into an **assessor-style Excel evidence pack** for key **Access Control (AC)** practices—fast, consistent, and easy to review.

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/securedbyjc/cmmc-ac-controls-demo.git
cd cmmc-ac-controls-demo

# Install dependencies (choose the one your repo uses)
pip install -r exporter/requirements.txt
# pip install -r requirements.txt

# Run the demo
python exporter/main.py

# Output folder:
# output/cmmc_ac_assessment_[timestamp].xlsx

✨ Features
🔧 Automated Evidence Generation

Pulls from mock IdP/AD user access, VPN/remote logs, and config stubs

Validates six AC controls with test notes

Produces an Excel evidence pack with hyperlinks and summaries

📚 Practice Mapping (6 AC controls)

AC.L2-3.1.1 — Authorized user access

AC.L2-3.1.3 — Flow of CUI

AC.L2-3.1.6 — Session lock

AC.L2-3.1.7 — Identifier reuse

AC.L2-3.1.12 — Remote access control

AC.L2-3.1.20 — External connections control

📦 Evidence Bundle Generation

Timestamped deliverables

Hyperlinked artifacts (policy, screenshots, config)

Test procedures and results

Executive summary + color status

📊 Professional Excel Output

Color-coded status (Green = Compliant, Yellow = Partial, Red = Non-Compliant)

Per-control tabs with mapped practice IDs

Summary dashboard and gap list

Print-ready formatting

🎬 Demo

Before: Raw Security Data (JSON)

{
  "finding": {
    "id": "REMOTE_ACCESS_POLICY",
    "source": "vpn_gateway",
    "severity": "HIGH",
    "control": "AC.L2-3.1.12",
    "details": "Split tunneling allowed for 2 users"
  }
}

**After: Audit-Ready Excel (example)**

| Control        | CMMC Practice | Evidence (examples)               | Test result                               | Status     | Finding                        |
|----------------|---------------|-----------------------------------|-------------------------------------------|:----------:|--------------------------------|
| Remote Access  | AC.L2-3.1.12  | VPN config; user list; policy PDF | 10 users sampled; 2 split-tunnel detected | ⚠️ Partial | 2 users non-conformant         |
| User Access    | AC.L2-3.1.1   | Access matrix; review attestation | 10/10 correct role assignment             | ✅ Pass    | None                           |
| External Conns | AC.L2-3.1.20  | Connection inventory; monitor log | Continuous monitor active                  | ✅ Pass    | 2 vendor attestations expiring |

📈 Why This Matters

For GRC teams

90% time reduction on evidence packaging

Instant practice mapping and consistent deliverables

Fewer last-minute scrambles

For organizations

Faster assessments → lower cost

Better visibility into gaps → reduced risk

Standardized evidence across business units

For the DIB ecosystem

Practical automation blueprint for NIST 800-171 / CMMC L2

Encourages standardized reporting and review

🧩 Architecture

flowchart LR
  A[Security Signals\n(IdP/AD, VPN, SIEM, MDM)] --> B[Data Processor]
  B --> C[Practice Mapper\n(CMMC L2 AC)]
  C --> D[Excel Generator]
  D --> E[Evidence Bundle]
  B -. Continuous Monitor .-> F[Alerts/Findings]

📁 Project Structure

cmmc-ac-controls-demo/
├─ exporter/
│  ├─ main.py                 # Assessment engine
│  └─ requirements.txt        # Python dependencies
├─ mock_data/
│  ├─ access_matrix.json      # User access data (mock)
│  ├─ remote_access.json      # VPN/remote access (mock)
│  └─ external_connections.json
├─ evidence_samples/          # Example artifacts
│  ├─ policies/
│  └─ screenshots/
├─ output/                    # Generated assessments
└─ README.md


🎓 Educational Purpose
This demo is designed to:

Show the art of the possible for CMMC evidence automation

Provide a learning resource for compliance engineers

Demonstrate integration patterns with security tools

Inspire standardized assessor-friendly outputs

Note: Uses simplified mappings and sample data. Production deployments must implement all 110 practices with real integrations.

🚀 Taking This to Production
Planned capabilities (example roadmap):

✅ Real-time API integrations (IdP, VPN, SIEM, MDM)

✅ Role-based access and audit trail

✅ Automated scheduling and distribution

✅ Dashboard (tech vs. administrative coverage)

✅ Export pipelines (Prevail, eMASS)

✅ Multi-environment support: AWS GovCloud (US), Microsoft GCC High, Google Cloud Assured Workloads

🔒 Enterprise auth (SSO/SAML) and tenant isolation

📈 Advanced correlation and continuous monitoring

🤝 Contributing
Contributions welcome:

Additional CMMC practices and mappings

New tool integrations

Report/evidence template improvements

Bug fixes and docs

Please open issues and PRs with clear repro steps.

📚 Resources
NIST 800-171 (Rev. 2)

CMMC Assessment Guides

FedRAMP (Ref. for reporting rigor)

CISA guidance on continuous monitoring

👥 About Eagle Defense Systems
Eagle Defense Systems (EDS) specializes in Governance-Ops-as-a-Service for defense contractors and federal system integrators—bridging cloud-native security tooling with compliance frameworks.

Services

🛡️ CMMC Assessment Readiness

📈 Automated Compliance Reporting

🔌 GRC Tool Integration

📡 Continuous Compliance Monitoring

🧭 Custom Framework Development

📬 Contact
Email: info@eagledefensesys.tech

Website: eagledefensesys.tech

LinkedIn: Eagle Defense Systems

📄 License
Released under the MIT License. See LICENSE for details.

⚖️ Disclaimer
Educational demonstration only. Not production-ready without full control coverage, validated integrations, and security review. No warranty, express or implied.

Featured on Aspire Cyber | Open Source Education
Transforming compliance from a burden into a competitive advantage
🌟 Star this repo if you find it helpful!

