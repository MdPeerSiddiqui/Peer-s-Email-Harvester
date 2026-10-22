#!/usr/bin/env python3
r"""
================================================================================
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
                                                                                          
  ⚡ PEER'S EMAIL HARVESTER & SE PRETEXTING ANALYZER — Day 02 ⚡
  Developed under Sqrock IT Solution — Alpha 2 Cybersecurity Internship
================================================================================
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from urllib.parse import urlparse
import requests

# Cross-platform color styling with graceful fallback
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    C_CYAN = Fore.CYAN
    C_GREEN = Fore.GREEN
    C_YELLOW = Fore.YELLOW
    C_RED = Fore.RED
    C_MAGENTA = Fore.MAGENTA
    C_WHITE = Fore.WHITE
    C_BRIGHT = Style.BRIGHT
    C_DIM = Style.DIM
    C_RESET = Style.RESET_ALL
except ImportError:
    C_CYAN = "\033[36m"
    C_GREEN = "\033[32m"
    C_YELLOW = "\033[33m"
    C_RED = "\033[31m"
    C_MAGENTA = "\033[35m"
    C_WHITE = "\033[37m"
    C_BRIGHT = "\033[1m"
    C_DIM = "\033[2m"
    C_RESET = "\033[0m"

# Ensure UTF-8 printing in Windows terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

BANNER = rf"""{C_CYAN}{C_BRIGHT}
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
{C_RESET}
{C_YELLOW}{C_BRIGHT} ⚡ PEER'S EMAIL HARVESTER & SE PRETEXTING ANALYZER v1.0 ⚡{C_RESET}
{C_WHITE}{C_DIM} [★] Developed for Sqrock IT Solution | Alpha 2 Cybersecurity Internship (Day 02){C_RESET}
{C_CYAN}{"=" * 80}{C_RESET}
"""

# Robust RFC-compliant email extraction regex
EMAIL_REGEX = re.compile(
    r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]*[a-zA-Z]{2,}",
    re.IGNORECASE
)


def analyze_pretexting_risk(email: str) -> dict:
    """Analyze harvested email to predict attacker social engineering pretexts."""
    username, _, domain = email.partition("@")
    user_lower = username.lower()

    if any(k in user_lower for k in ["billing", "invoice", "finance", "payment", "account"]):
        return {
            "department": "Finance & Accounts",
            "risk_level": "CRITICAL",
            "threat_vector": "Business Email Compromise (BEC), Fake Vendor Invoice Fraud",
            "attacker_pretext": "Impersonating executive/vendor demanding urgent wire transfer for overdue invoice."
        }
    elif any(k in user_lower for k in ["hr", "career", "recruit", "talent", "job"]):
        return {
            "department": "Human Resources",
            "risk_level": "HIGH",
            "threat_vector": "Weaponized Attachment Lures (Malicious CV / Resume)",
            "attacker_pretext": "Job applicant emailing macro-enabled DOCX/PDF purporting to be an executive portfolio."
        }
    elif any(k in user_lower for k in ["it", "support", "helpdesk", "admin", "service"]):
        return {
            "department": "IT Operations",
            "risk_level": "CRITICAL",
            "threat_vector": "Credential Harvesting & Fake Maintenance Portals",
            "attacker_pretext": "Fake notification alerting user of mandatory MFA update or password expiration."
        }
    elif any(k in user_lower for k in ["security", "soc", "compliance", "abuse"]):
        return {
            "department": "Security Operations",
            "risk_level": "HIGH",
            "threat_vector": "Incident Response Impersonation",
            "attacker_pretext": "Urgent alert claiming recipient's PC is sending malware, requesting immediate remote access."
        }
    else:
        return {
            "department": "General / Inquiries",
            "risk_level": "MEDIUM",
            "threat_vector": "Organizational Fingerprinting & Phishing Pivot",
            "attacker_pretext": "General inquiries designed to map out active internal employee names and hierarchy."
        }


def extract_emails_from_text(content: str) -> list:
    """Extract, clean, and deduplicate email addresses from raw text or HTML."""
    raw_matches = EMAIL_REGEX.findall(content)
    cleaned = set()
    for email in raw_matches:
        # Strip trailing dots or dashes often caught in punctuation
        email_clean = email.strip(".-'\"<>")
        if email_clean and "." in email_clean.split("@")[-1]:
            cleaned.add(email_clean.lower())
    return sorted(list(cleaned))


def harvest_from_target(target_path_or_url: str) -> dict:
    """Fetch content from HTTP URL or local HTML file and extract emails."""
    scan_time = datetime.now()
    report = {
        "tool": "PEER'S Email Harvester & SE Pretexting Analyzer",
        "program": "Sqrock IT Solution — Alpha 2 Cybersecurity Internship",
        "day": 2,
        "timestamp": scan_time.isoformat(),
        "target": target_path_or_url,
        "source_type": "URL" if target_path_or_url.startswith(("http://", "https://")) else "Local File",
        "harvested_count": 0,
        "emails": [],
        "risk_breakdown": {}
    }

    print(f"\n{C_GREEN}{C_BRIGHT}[*] TARGET IDENTIFIED :{C_RESET} {C_WHITE}{C_BRIGHT}{target_path_or_url}{C_RESET}")
    print(f"{C_GREEN}[*] SOURCE TYPE       :{C_RESET} {report['source_type']}")
    print(f"{C_GREEN}[*] TIME OF HARVEST   :{C_RESET} {scan_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{C_CYAN}{'-' * 80}{C_RESET}")

    # Step 1: Content Retrieval
    print(f"\n{C_YELLOW}{C_BRIGHT}[1] RETRIEVING TARGET CONTENT...{C_RESET}")
    html_text = ""
    try:
        if report["source_type"] == "URL":
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OSINT-Lab/1.0"}
            resp = requests.get(target_path_or_url, headers=headers, timeout=10)
            resp.raise_for_status()
            html_text = resp.text
            print(f"    {C_GREEN}[+] HTTP Response Code   :{C_RESET} {resp.status_code} OK")
            print(f"    {C_GREEN}[+] Payload Size Received:{C_RESET} {len(html_text):,} bytes")
        else:
            if not os.path.exists(target_path_or_url):
                print(f"    {C_RED}[!] Error: File '{target_path_or_url}' not found!{C_RESET}")
                return report
            with open(target_path_or_url, "r", encoding="utf-8", errors="ignore") as f:
                html_text = f.read()
            print(f"    {C_GREEN}[+] Local File Loaded    :{C_RESET} {target_path_or_url}")
            print(f"    {C_GREEN}[+] File Size Read       :{C_RESET} {len(html_text):,} bytes")
    except Exception as e:
        print(f"    {C_RED}[!] Retrieval Failed     :{C_RESET} {e}")
        return report

    # Step 2: Regular Expression Scanning
    print(f"\n{C_YELLOW}{C_BRIGHT}[2] EXECUTING REGEX HARVESTING ENGINE...{C_RESET}")
    harvested = extract_emails_from_text(html_text)
    report["harvested_count"] = len(harvested)
    print(f"    {C_GREEN}[+] Unique Email Addresses Discovered: {C_BRIGHT}{len(harvested)}{C_RESET}")

    if not harvested:
        print(f"    {C_WHITE}{C_DIM}[~] No matching email patterns found in target document.{C_RESET}")
        return report

    # Step 3: Social Engineering Pretexting Analysis
    print(f"\n{C_YELLOW}{C_BRIGHT}[3] SOCIAL ENGINEERING & PRETEXTING THREAT ANALYSIS...{C_RESET}")
    print(f"{C_CYAN}{'-' * 80}{C_RESET}")

    for idx, email in enumerate(harvested, 1):
        pretext_info = analyze_pretexting_risk(email)
        risk_color = C_RED if pretext_info["risk_level"] == "CRITICAL" else (C_YELLOW if pretext_info["risk_level"] == "HIGH" else C_CYAN)

        email_entry = {
            "index": idx,
            "email": email,
            "department": pretext_info["department"],
            "risk_level": pretext_info["risk_level"],
            "threat_vector": pretext_info["threat_vector"],
            "attacker_pretext": pretext_info["attacker_pretext"]
        }
        report["emails"].append(email_entry)

        print(f"  {C_WHITE}[{idx:02d}]{C_RESET} {C_GREEN}{C_BRIGHT}{email:<36}{C_RESET} | Dept: {pretext_info['department']:<18} | Risk: {risk_color}{pretext_info['risk_level']}{C_RESET}")
        print(f"       {C_WHITE}├── Threat Vector   :{C_RESET} {pretext_info['threat_vector']}")
        print(f"       {C_WHITE}└── Attacker Pretext:{C_RESET} {C_DIM}{pretext_info['attacker_pretext']}{C_RESET}")

    # Step 4: Summary & Report Saving
    print(f"\n{C_CYAN}{'=' * 80}{C_RESET}")
    print(f"{C_GREEN}{C_BRIGHT}                      ✔ HARVESTING COMPLETED SUCCESSFULLY{C_RESET}")
    print(f"{C_CYAN}{'=' * 80}{C_RESET}")

    # Output saving
    reports_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reports")
    os.makedirs(reports_dir, exist_ok=True)
    clean_target_name = re.sub(r"[^a-zA-Z0-9.-]", "_", os.path.basename(target_path_or_url) or "target")
    output_json = os.path.join(reports_dir, f"day02_harvested_{clean_target_name}.json")
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)
    print(f"\n{C_WHITE}[★] Structured JSON Deliverable Saved : {C_GREEN}{output_json}{C_RESET}")

    return report


def main():
    print(BANNER)
    parser = argparse.ArgumentParser(
        description="PEER'S Email Harvester & SE Pretexting Tool (Sqrock IT Solution Internship)"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="URL (http/https) or local HTML file path to scan",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run scan against the authorized local practice lab target",
    )

    args = parser.parse_args()
    target = args.target

    if args.demo:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        target = os.path.join(script_dir, "lab_target.html")
    elif not target:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        default_lab = os.path.join(script_dir, "lab_target.html")
        try:
            print(f"{C_YELLOW}[?] Enter Target URL or Local HTML File Path{C_RESET}")
            print(f"    {C_DIM}(Press ENTER to scan local practice lab target: lab_target.html){C_RESET}")
            user_input = input(f"{C_CYAN}    └── Target > {C_RESET}").strip()
            target = user_input if user_input else default_lab
        except (KeyboardInterrupt, EOFError):
            print(f"\n{C_RED}[!] Harvest aborted by user.{C_RESET}")
            sys.exit(0)

    harvest_from_target(target)


if __name__ == "__main__":
    main()
