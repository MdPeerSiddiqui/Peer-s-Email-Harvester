<div align="center">

# 📧 Email Harvester & Pretexting Threat Analyzer
### *Automated Email Extraction & Social Engineering Preparation Engine*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Track](https://img.shields.io/badge/Track-Cybersecurity%20Alpha%202-red?style=for-the-badge&logo=shield)](https://github.com/MdPeerSiddiqui)
[![Organization](https://img.shields.io/badge/Sqrock%20IT%20Solution-Cybersecurity-00C853?style=for-the-badge)](https://github.com/MdPeerSiddiqui)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Developed by <a href="https://github.com/MdPeerSiddiqui">Md Peer Siddiqui</a> | Sqrock IT Solution Internship (Day 02)</b>
</p>

---

</div>

## 📌 Overview

**Email Harvester & Pretexting Analyzer** is a Python-based open-source intelligence and social engineering preparation utility. It extracts email addresses from web pages and local HTML documents using RFC-compliant regular expressions and automatically performs **departmental threat modeling** to predict how adversaries could craft spear-phishing pretexts.

---

## ⚡ Core Capabilities

- 🔍 **Dual-Source Extraction**: Scrapes live HTTP/HTTPS web URLs and local offline HTML testbeds (`lab_target.html`).
- 🧠 **Pretexting Threat Modeling**: Maps scraped addresses to business departments (Finance, HR, IT Support, Security) and identifies predicted social engineering attack vectors (BEC, malicious macro CVs, fake MFA portals).
- 🧹 **Robust Regex Cleaning**: Normalizes casing, strips punctuation artifacts (trailing dots/quotes), and deduplicates results.
- 💾 **Automated Deliverables**: Automatically exports structured JSON audit deliverables into `reports/`.

---

## 🚀 Quickstart & Installation

```bash
# 1. Clone repository
git clone <your-repo-url>
cd day02_email_harvesting

# 2. Install dependencies
pip install requests colorama

# 3. Run the Harvester (Interactive or Demo)
python email_harvester.py --demo
```

---

## 🎮 Usage Examples

### 1. Interactive Mode
```bash
python email_harvester.py
# Press Enter to use the built-in lab_target.html or paste a target URL/file
```

### 2. Direct Command Mode
```bash
# Scan a local HTML testbed
python email_harvester.py lab_target.html

# Scan an authorized lab URL
python email_harvester.py http://your-authorized-lab.local
```

---

## 🛡️ Attacker vs. Defender Implications

* **Attacker View**: Uncovering public email aliases allows adversaries to skip generic spam filters and send high-conviction spear-phishing messages (e.g. sending fake invoices to `billing@` or weaponized resumes to `careers@`).
* **Defender View**: Organizations should avoid raw `mailto:` tags, use server-side forms with CAPTCHA, enforce strict DMARC/SPF/DKIM policies, and require out-of-band phone verification for payment modifications.

---

## ⚖️ Legal & Ethical Policy
**STRICTLY FOR AUTHORIZED LAB & EDUCATIONAL AUDITING.**  
Scanning must only be performed on domains you own, explicitly authorized testbeds, or local simulation environments. Compliance with the Indian IT Act 2000 and US CFAA is mandatory.
