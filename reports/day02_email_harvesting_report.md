# CYBERSECURITY INTERNSHIP — PRACTICAL LAB REPORT

## Day 02: Email Harvesting & Social Engineering Preparation

- **Intern Name:** Md Peer Siddiqui  
- **Organization:** Sqrock IT Solution  
- **Program / Track:** Alpha 2 Internship — Cybersecurity Track  
- **Date of Execution:** October 21–22, 2026  
- **Lab Environment:** Authorized Local Practice HTML Testbed (`lab_target.html` — Apex Dynamics Inc.)  
- **GitHub Repository:** [https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester](https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester)  

---

### 1. Objective

The primary objective of this exercise is to understand how email addresses can be identified, extracted, and collected from publicly accessible web page content using Python automation and regular expressions (`re`). Furthermore, the exercise evaluates how exposed contact metadata can be weaponized by threat actors to perform organizational profiling and craft convincing psychological pretexts for spear-phishing and Business Email Compromise (BEC) attacks.

---

### 2. Tools and Environment

- **Operating System:** Kali Linux 2026.2 (64-bit VirtualBox Lab VM) / Windows 11 Host
- **Python Version:** Python 3.11.9 / Python 3.14.0
- **`requests` (v2.34.2):** Used to retrieve target HTML documents over HTTP/HTTPS.
- **`re` (Python standard library):** Compiles and evaluates regular expressions to locate pattern matches adhering to the RFC 5322 email formatting standard.
- **`colorama` (v0.4.6):** Formats terminal output with color-coded risk severity banners.
- **Practice Target:** `lab_target.html` — A simulated corporate contact portal for *Apex Dynamics Inc.*, containing structured departmental contact listings.

---

### 3. Methodology

The lab was conducted following a systematic, non-invasive methodology:

1. **Target Environment Preparation:** An authorized local corporate communications directory (`lab_target.html`) was deployed containing realistic public department addresses.
2. **Automated Content Retrieval:** The script reads the page content (either by streaming the local document or making an HTTP GET request with custom User-Agent headers).
3. **Pattern Matching & Regular Expression Execution:** The raw DOM/HTML string is parsed using the compiled regular expression:
   `[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+`
4. **Data Normalization & Duplicate Removal:** Raw extracted tokens are cleaned of trailing HTML punctuation (`<`, `>`, `"`, `'`, `.`, `-`), converted to lowercase, and passed into Python's `set()` data structure to eliminate redundant occurrences.
5. **Pretexting Threat Modeling:** Each extracted email address prefix is parsed through a heuristic threat engine to categorize its business department (Finance, HR, IT Support, General) and map its primary attack vector.
6. **Verification & Audit Export:** Extracted results were cross-checked against the known ground-truth dataset in `lab_target.html` and saved to `reports/day02_harvested_lab_target.html.json`.

---

### 4. Implementation

The implementation was built as a modular CLI utility: **PEER'S Email Harvester & SE Pretexting Analyzer** (`email_harvester.py`).

#### Core Technical Logic:
```python
import re, requests

# RFC-compliant email regex
EMAIL_REGEX = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]{2,}", re.IGNORECASE)

def extract_emails_from_text(content: str) -> list:
    raw_matches = EMAIL_REGEX.findall(content)
    cleaned = set()
    for email in raw_matches:
        email_clean = email.strip(".-'\"<>")
        if email_clean and "." in email_clean.split("@")[-1]:
            cleaned.add(email_clean.lower())
    return sorted(list(cleaned))
```

#### Step-by-Step Explanation:
1. **Input Handling:** The script accepts a target via CLI arguments (`--demo`, local file path, or remote URL). If none is specified, it prompts the analyst interactively.
2. **Regex Scanning:** `re.findall()` iterates through the entire payload string in a single linear pass to isolate any token matching standard email address structures.
3. **Punctuation Trimming:** Any punctuation trapped inside HTML attributes (such as `href="mailto:user@domain.com."`) is sanitized.
4. **Deduplication:** Converting matches to a `set` guarantees that addresses appearing multiple times across navigation bars, footers, and tables are counted exactly once.
5. **Department Classification:** Custom rule sets evaluate keywords (`billing`, `careers`, `it-support`) to assign threat levels (`CRITICAL`, `HIGH`, `MEDIUM`).

---

### 5. Results and Verification

- **Number of unique addresses discovered:** **7**
- **Payload size parsed:** 2,489 bytes
- **Harvest status:** 100% Successful (Zero false positives, zero missed entries)

#### Extracted Results Table:

| # | Harvested Email Address | Department | Risk Level | Primary Threat Vector |
|:---:|:---|:---|:---:|:---|
| **01** | `billing-invoices@apexdynamics-lab.local` | Finance & Accounts | **CRITICAL** | Business Email Compromise (BEC), Fake Vendor Invoice Fraud |
| **02** | `careers@apexdynamics-lab.local` | Human Resources | **HIGH** | Weaponized Attachment Lures (Malicious CV / Resume) |
| **03** | `finance.desk@apexdynamics-lab.local` | Finance & Accounts | **CRITICAL** | CEO Impersonation Fraud & Unauthorized Wire Transfers |
| **04** | `hr-department@apexdynamics-lab.local` | Human Resources | **HIGH** | Spear-Phishing / Employee Identity Verification Lures |
| **05** | `info@apexdynamics-lab.local` | General / Inquiries | **MEDIUM** | Organizational Fingerprinting & Phishing Pivot |
| **06** | `it-support@apexdynamics-lab.local` | IT Operations | **CRITICAL** | Credential Harvesting & Fake SSO / MFA Update Portals |
| **07** | `security-ops@apexdynamics-lab.local` | IT Operations | **CRITICAL** | Incident Response Spoofing & Remote Access Scams |

#### Verification:
Each identified address was verified by manual inspection of `lab_target.html`. The scanner accurately extracted all 7 embedded addresses, including both plaintext visible email labels and values inside HTML `href="mailto:..."` attributes.

---

### 6. Security Analysis: Potential Misuse

In real-world cyber attacks, adversaries do not harvest emails simply to generate bulk spam. Scraped departmental listings form the intelligence baseline for multi-stage social engineering campaigns:

1. **Targeted Phishing & Spear-Phishing:**  
   Addresses matching `careers@` or `hr-department@` are targeted with weaponized resumes containing macro-enabled Microsoft Word documents (`.docm`) or malicious PDF payloads. HR personnel expect inbound files from strangers, making them unusually vulnerable.
2. **Business Email Compromise (BEC):**  
   Harvesting `billing-invoices@` enables attackers to monitor supplier payment cycles and spoof vendor correspondence demanding urgent wire transfer rerouting to fraudulent bank accounts.
3. **Internal IT Impersonation:**  
   Harvesting `it-support@` enables attackers to craft realistic internal alert templates ("Mandatory Password Reset" or "VPN Gateway Migration") directing employees to cloned credential-harvesting landing pages.
4. **Organizational Footprinting:**  
   Public contact lists reveal internal naming conventions (e.g., `firstname.lastname@company.com`), department hierarchies, and external third-party software dependencies.
5. **Absence of Consent:**  
   Public visibility of an address on a corporate website does not imply consent to receive deceptive, unsolicited, or spoofed communications.

---

### 7. Defensive Measures

To defend against automated email harvesting and subsequent pretexting attacks, organizations should deploy multi-layered defenses:

1. **Contact Obfuscation:**  
   Replace plaintext email addresses and `mailto:` links on public websites with server-side contact web forms protected by modern CAPTCHA mechanisms (e.g., Cloudflare Turnstile or Google reCAPTCHA v3).
2. **Email Authentication Protocols (SPF, DKIM, DMARC):**  
   - **SPF (Sender Policy Framework):** Specifies authorized mail servers for the domain.  
   - **DKIM (DomainKeys Identified Mail):** Cryptographically signs outbound messages to prove message integrity.  
   - **DMARC (Domain-based Message Authentication):** Enforces a strict `p=reject` policy so receivers reject spoofed emails claiming to originate from the organization.
3. **Inbound Attachment Sandboxing & Email Filtering:**  
   Deploy email security gateways (e.g., Proofpoint, Mimecast) that dynamically detonate inbound attachments and rewrite URLs to protect against zero-day links.
4. **Out-of-Band Verification Policies:**  
   Establish mandatory dual-authorization and telephone callback protocols for any financial transaction, invoice modification, or wire transfer request over a defined threshold.

---

### 8. Ethical Compliance and Limitations

- **Authorization Scope:**  
  All testing was performed strictly on local, non-production laboratory targets (`lab_target.html`). At no point were external, unauthorized corporate networks, third-party mail servers, or live individuals probed.
- **Legal Compliance:**  
  All actions adhered to the **Indian Information Technology Act, 2000 (Section 43 & 66)**, the **US Computer Fraud and Abuse Act (CFAA)**, and Sqrock IT Solution internship guidelines.
- **Technical Limitations:**  
  - The script parses textual DOM content; it does not render JavaScript-obfuscated email strings (e.g., emails assembled dynamically via client-side JS or embedded as raster images).
  - Regular expressions alone identify potential email strings but do not verify whether the recipient mailbox actively exists or accepts mail.

---

### 9. Conclusion

This laboratory exercise successfully validated the fundamentals of automated email harvesting using Python and regular expressions. By building **PEER'S Email Harvester**, the workflow demonstrated how trivial it is for an external entity to map an organization's public contact structure in seconds. 

The primary takeaway is that reconnaissance automation enables high-conviction pretexting. Robust defenses must combine technical email safeguards (DMARC `p=reject`, contact form obfuscation) with continuous human awareness training.

---

### Appendix

- **Appendix A: Complete Script:** [`email_harvester.py`](https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester/blob/main/email_harvester.py)
- **Appendix B: GitHub Repository:** [https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester](https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester)
- **Appendix C: Actual Results List:** Saved in [`reports/day02_harvested_lab_target.html.json`](https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester/blob/main/reports/day02_harvested_lab_target.html.json)
- **Appendix D: Execution Proof:** Verified live on Kali Linux 2026.2 (`day02_kali_exec_part1.png`, `day02_kali_exec_part2.png`).
