# Day 02 Deliverable: Email Harvesting & Social Engineering Preparation Report

- **Intern Name:** Md Peer Siddiqui
- **Organization:** Sqrock IT Solution
- **Program:** Alpha 2 Internship — Cybersecurity Track
- **Topic:** Day 02 — Email Harvesting & Pretexting Fundamentals
- **Target Scope:** Authorized Local Practice Lab (`lab_target.html`)
- **Date:** October 21, 2026

---

## 1. Objective
To understand how public-facing email addresses can be scraped from web documents using Python and regular expressions (`re`), and to analyze how adversaries weaponize harvested email directories to construct targeted social engineering pretexts.

---

## 2. Tools & Technologies Used
* **Python 3.14**: Core programming environment.
* **Requests**: HTTP client for retrieving remote web resources.
* **Regular Expressions (`re`)**: Pattern extraction engine using RFC-compliant email expressions.
* **Local Lab Server / HTML Testbed**: Simulated corporate directory (`lab_target.html`) ensuring 100% ethical compliance without touching unauthorized systems.

---

## 3. Methodology & Execution

1. **Target Setup**: A realistic corporate contact page for a simulated company (*Apex Dynamics Inc.*) was deployed locally. The page includes public contact points across Finance, Human Resources, IT Support, and Executive Management.
2. **Automated Retrieval**: The Python tool accesses the target via standard HTTP GET or file streaming.
3. **Pattern Matching & Deduplication**: The HTML DOM text is processed through regex `[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+` to extract raw addresses, normalize capitalization, strip punctuation artifacts, and deduplicate entries into an ordered set.
4. **Pretexting Risk Assessment**: The script evaluates each email address prefix (e.g., `billing-`, `careers-`, `it-support-`) to map the threat vector and determine the highest-likelihood attack pretext.

---

## 4. Practical Results & Harvested Findings

The scanner extracted **7 unique email addresses** and categorized each address according to departmental risk:

| # | Harvested Email Address | Target Department | Risk Level | Primary Threat Vector |
|:---:|:---|:---|:---:|:---|
| **01** | `billing-invoices@apexdynamics-lab.local` | Finance & Accounts | **CRITICAL** | Business Email Compromise (BEC) & Vendor Wire Fraud |
| **02** | `careers@apexdynamics-lab.local` | Human Resources | **HIGH** | Malicious CV / Macro-enabled Attachment Lures |
| **03** | `finance.desk@apexdynamics-lab.local` | Finance & Accounts | **CRITICAL** | Urgent CEO Fraud / Payment Redirection |
| **04** | `hr-department@apexdynamics-lab.local` | Human Resources | **HIGH** | Spear-Phishing / Fake Employee Verification |
| **05** | `info@apexdynamics-lab.local` | General Desk | **MEDIUM** | Organizational Mapping & Reconnaissance Pivot |
| **06** | `it-support@apexdynamics-lab.local` | IT Operations | **CRITICAL** | Credential Harvesting & Fake MFA Update Portals |
| **07** | `security-ops@apexdynamics-lab.local` | IT Operations | **CRITICAL** | Fake Incident Alerts & Remote Access Lures |

---

## 5. Security & Pretexting Threat Analysis

### A. Attacker Perspective (How Adversaries Weaponize Harvested Data)
* **Pretexting Craftsmanship**: Threat actors do not send generic spam. When an attacker harvests `billing-invoices@...`, they craft a convincing pretext pretending to be an existing supplier demanding urgent ACH update payments before contract termination.
* **Department-Specific Targeting**:
  * Targeting `careers@...` allows adversaries to bypass technical web perimeter firewalls by emailing macro-enabled `.docm` or `.pdf` files disguised as candidate resumes.
  * Targeting `it-support@...` allows attackers to send fake IT announcements ("Mandatory SSO Migration — Update Password") directing users to cloned credential harvesting landing pages.

### B. Defender Perspective (Mitigation & Countermeasures)
1. **Contact Obfuscation**: Avoid exposing raw `mailto:` tags in raw HTML. Use server-side web forms with CAPTCHA validation.
2. **Email Security Protocols**: Implement strict **SPF (Sender Policy Framework)**, **DKIM (DomainKeys Identified Mail)**, and **DMARC (reject policy)** to prevent direct domain spoofing.
3. **Advanced Threat Protection (ATP)**: Deploy email sandboxing to analyze inbound attachments and quarantine suspicious links.
4. **Security Awareness Training**: Train finance and HR personnel to perform out-of-band verification (phone callback) before processing financial or credential requests.

---

## 6. Conclusion
This exercise demonstrated the efficiency of regex-driven email harvesting and highlighted why public contact exposure is a primary precursor to targeted social engineering. Ethical boundaries were strictly maintained by executing all scans against local simulation targets.

**Legal Scope**: Strictly authorized educational lab environment complying with IT Act 2000 and CFAA standards.
