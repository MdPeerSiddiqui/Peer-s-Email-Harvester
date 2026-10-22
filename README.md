<div align="center">

# 📧 PEER'S EMAIL HARVESTER
### *Automated Email Extraction & Pretexting Threat Modeling Engine*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Track](https://img.shields.io/badge/Track-Cybersecurity%20Alpha%202-red?style=for-the-badge&logo=shield)](https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester)
[![Organization](https://img.shields.io/badge/Issuing%20Body-Sqrock%20IT%20Solution-00C853?style=for-the-badge)](https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Engineered by <a href="https://github.com/MdPeerSiddiqui">Md Peer Siddiqui</a> under Sqrock IT Solution — Alpha 2 Internship (Day 02)</b>
</p>

---

</div>

## 🖥️ Interactive Terminal Interface

```text
  _____  ______ ______ _____  _  _____ 
 |  __ \|  ____|  ____|  __ \(_)/ ____|
 | |__) | |__  | |__  | |__) |_| (___  
 |  ___/|  __| |  __| |  _  /   \___ \ 
 | |    | |____| |____| | \ \   ____) |
 |_|    |______|______|_|  \_\ |_____/ 
  ______ __  __          _____ _        _    _                               _            
 |  ____|  \/  |   /\   |_   _| |      | |  | |                             | |           
 | |__  | \  / |  /  \    | | | |      | |__| | __ _ _ ____   _____  ___ ___| |_ ___ _ __ 
 |  __| | |\/| | / /\ \   | | | |      |  __  |/ _` | '__\ \ / / _ \/ __/ __| __/ _ \ '__|
 | |____| |  | |/ ____ \ _| |_| |____  | |  | | (_| | |   \ V /  __/\__ \__ \ ||  __/ |   
 |______|_|  |_/_/    \_\_____|______| |_|  |_|\__,_|_|    \_/ \___||___/___/\__\___|_|   

 ⚡ PEER'S EMAIL HARVESTER & SE PRETEXTING ANALYZER v1.0 ⚡
 [★] Developed for Sqrock IT Solution | Alpha 2 Cybersecurity Internship (Day 02)
================================================================================

[*] TARGET IDENTIFIED : lab_target.html
[*] SOURCE TYPE       : Local File
[*] TIME OF HARVEST   : 2026-10-22 07:39:08 UTC
--------------------------------------------------------------------------------

[1] RETRIEVING TARGET CONTENT...
    [+] Local File Loaded    : lab_target.html
    [+] File Size Read       : 2,489 bytes

[2] EXECUTING REGEX HARVESTING ENGINE...
    [+] Unique Email Addresses Discovered: 7

[3] SOCIAL ENGINEERING & PRETEXTING THREAT ANALYSIS...
--------------------------------------------------------------------------------
  [01] billing-invoices@apexdynamics-lab.local | Dept: Finance & Accounts | Risk: CRITICAL
       ├── Threat Vector   : Business Email Compromise (BEC), Fake Vendor Invoice Fraud
       └── Attacker Pretext: Impersonating executive/vendor demanding urgent wire transfer for overdue invoice.
  [02] careers@apexdynamics-lab.local       | Dept: Human Resources    | Risk: HIGH
       ├── Threat Vector   : Weaponized Attachment Lures (Malicious CV / Resume)
       └── Attacker Pretext: Job applicant emailing macro-enabled DOCX/PDF purporting to be an executive portfolio.
  [03] finance.desk@apexdynamics-lab.local  | Dept: Finance & Accounts | Risk: CRITICAL
       ├── Threat Vector   : Business Email Compromise (BEC), Fake Vendor Invoice Fraud
       └── Attacker Pretext: Impersonating executive/vendor demanding urgent wire transfer for overdue invoice.
  [04] hr-department@apexdynamics-lab.local | Dept: Human Resources    | Risk: HIGH
       ├── Threat Vector   : Weaponized Attachment Lures (Malicious CV / Resume)
       └── Attacker Pretext: Job applicant emailing macro-enabled DOCX/PDF purporting to be an executive portfolio.
  [05] info@apexdynamics-lab.local          | Dept: General / Inquiries | Risk: MEDIUM
       ├── Threat Vector   : Organizational Fingerprinting & Phishing Pivot
       └── Attacker Pretext: General inquiries designed to map out active internal employee names and hierarchy.
  [06] it-support@apexdynamics-lab.local    | Dept: IT Operations      | Risk: CRITICAL
       ├── Threat Vector   : Credential Harvesting & Fake Maintenance Portals
       └── Attacker Pretext: Fake notification alerting user of mandatory MFA update or password expiration.
  [07] security-ops@apexdynamics-lab.local  | Dept: IT Operations      | Risk: CRITICAL
       ├── Threat Vector   : Credential Harvesting & Fake Maintenance Portals
       └── Attacker Pretext: Fake notification alerting user of mandatory MFA update or password expiration.

================================================================================
                      ✔ HARVESTING COMPLETED SUCCESSFULLY
================================================================================

[★] Structured JSON Deliverable Saved : reports/day02_harvested_lab_target.html.json
```

---

## 📌 What is PEER'S Email Harvester?

**PEER'S Email Harvester** is a command-line reconnaissance and social engineering preparation tool written in Python. It scrapes publicly accessible email addresses from online web pages and offline HTML testbeds using regular expressions. Beyond extraction, it automatically applies a **Pretexting Threat Modeling Engine** that identifies the department, evaluates the organizational risk level, and predicts how an adversary would weaponize the address for targeted phishing.

---

## ⚡ Key Capabilities

* 🌐 **Dual Target Scanning**: Works on remote HTTP/HTTPS URLs or local HTML practice files (`lab_target.html`) with zero external network dependencies.
* 🧹 **RFC-Compliant Regex Normalization**: Extracts valid email patterns, filters plus-addressing, cleans trailing punctuation artifacts, and deduplicates with `set()`.
* 🧠 **Automated Pretexting Modeling**: Classifies addresses into Finance, HR, IT Support, Security, or General Inquiries.
* 🛡️ **Threat Vector Mapping**: Predicts attacks such as Business Email Compromise (BEC), weaponized macro resumes, and credential harvesting portals.
* 💾 **Audit-Ready Reporting**: Exports structured JSON deliverables into `reports/` for SOC logs and internship submissions.

---

## 🚀 Installation Guide (Cross-Platform)

### 🐧 Option 1: Linux / Kali Linux

Open your terminal and run:

```bash
# 1. Clone repository
git clone https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester.git
cd Peer-s-Email-Harvester

# 2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Run scanner on practice lab target
python3 email_harvester.py --demo
```

---

### 🪟 Option 2: Windows (PowerShell or Command Prompt)

Open PowerShell and run:

```powershell
# 1. Clone repository
git clone https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester.git
cd Peer-s-Email-Harvester

# 2. Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Run scanner on practice lab target
python email_harvester.py --demo
```

---

### 🍎 Option 3: macOS (Apple Silicon / Intel)

Open Terminal and run:

```bash
# 1. Clone repository
git clone https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester.git
cd Peer-s-Email-Harvester

# 2. Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Run scanner
python3 email_harvester.py --demo
```

---

## 🎮 How to Run

### 1. Demo Mode (Scans built-in local practice target)
```bash
python email_harvester.py --demo
```

### 2. Interactive Mode (Simply prompts for target)
```bash
python email_harvester.py
```
*Prompt:*
```text
[?] Enter Target URL or Local HTML File Path
    (Press ENTER to scan local practice lab target: lab_target.html)
    └── Target > 
```

### 3. Direct File / URL Scanning
```bash
# Scan a local HTML file
python email_harvester.py lab_target.html

# Scan an authorized lab domain
python email_harvester.py http://your-authorized-lab.local
```

---

## 📂 Repository Contents

```text
Peer-s-Email-Harvester/
├── email_harvester.py              # 🚀 Main CLI Harvester & Pretexting Engine
├── lab_target.html                 # 🎯 Simulated Practice Target (Apex Dynamics Inc.)
├── requirements.txt                # 📋 Python Dependencies (requests, colorama)
├── README.md                       # 📖 Tool documentation & quickstart
├── LICENSE                         # ⚖️ MIT Open Source License
└── reports/                        # 📊 Official PDF Deliverable & JSON Reports
    ├── Day02_Email_Harvesting_Report_Sqrock_MdPeerSiddiqui.pdf
    ├── day02_email_harvesting_report.md
    └── day02_harvested_lab_target.html.json
```

---

## 🛡️ Attacker vs. Defender Security Insights

| Perspective | Security Application |
| :--- | :--- |
| **Attacker (Pretexting Strategy)** | Uncovering role-specific email aliases enables tailored spear-phishing (e.g. sending fake vendor invoices to `billing@` or malicious macro resumes to `careers@`) while bypassing generic spam filters. |
| **Defender (Countermeasures)** | Organizations must replace plaintext `mailto:` tags with server-side web contact forms protected by CAPTCHA, enforce strict SPF/DKIM/DMARC (`p=reject`), and implement mandatory out-of-band verification for payment requests. |

---

## 🏛️ Internship Program Attribution
This tool was engineered for **Day 02** of the **Alpha 2 Internship — Cybersecurity Track** organized by **Sqrock IT Solution**.

---

## ⚖️ Legal & Ethical Policy
**FOR EDUCATIONAL, RESEARCH, AND AUTHORIZED AUDITING ONLY.**  
Harvesting must only be performed on domains you own, explicitly authorized testbeds, or local simulation environments (`lab_target.html`). All activities must comply with the Indian Information Technology Act (2000), US Computer Fraud and Abuse Act (CFAA), and applicable local data privacy laws.

---

<div align="center">
  <sub>Built with ❤️ by Md Peer Siddiqui • Powered by Sqrock IT Solution</sub>
</div>
