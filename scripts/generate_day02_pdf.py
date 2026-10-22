"""
Generate Executive PDF Report for Day 2 Deliverable
Sqrock IT Solution — Alpha 2 Internship (Cybersecurity Track)
Author: Md Peer Siddiqui
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, PageBreak
)

def create_day02_report(output_pdf_path=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if output_pdf_path is None:
        output_pdf_path = os.path.join(base_dir, "reports", "Day02", "Day02_Email_Harvesting_Report_Sqrock_MdPeerSiddiqui.pdf")
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom palette
    primary_color = colors.HexColor("#0f172a")     # Dark slate
    accent_color = colors.HexColor("#0284c7")      # Cyber blue
    risk_critical = colors.HexColor("#dc2626")     # Red
    risk_high = colors.HexColor("#ea580c")         # Orange
    bg_light = colors.HexColor("#f8fafc")
    text_dark = colors.HexColor("#1e293b")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=primary_color,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=accent_color,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=primary_color,
        spaceBefore=7,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=text_dark,
        spaceAfter=4
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=primary_color
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=text_dark
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor("#0f172a")
    )

    story = []

    # 1. Header Banner & Title
    story.append(Paragraph("CYBERSECURITY INTERNSHIP — PRACTICAL LAB REPORT", subtitle_style))
    story.append(Paragraph("DAY 02: Email Harvesting & Social Engineering Preparation", title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_color, spaceBefore=2, spaceAfter=8))

    # 2. Executive Metadata Grid
    meta_data = [
        [
            Paragraph("Intern Name:", meta_label), Paragraph("Md Peer Siddiqui", meta_val),
            Paragraph("Program:", meta_label), Paragraph("Alpha 2 — Cybersecurity Track", meta_val)
        ],
        [
            Paragraph("Issuing Body:", meta_label), Paragraph("Sqrock IT Solution", meta_val),
            Paragraph("Date of Execution:", meta_label), Paragraph("October 21, 2026", meta_val)
        ],
        [
            Paragraph("Target Environment:", meta_label), Paragraph("Local Lab Simulation (Apex Dynamics Inc.)", meta_val),
            Paragraph("Primary Tools:", meta_label), Paragraph("Python 3.14, Requests, Regex (re)", meta_val)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[90, 180, 100, 170])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # 3. Methodology & Curriculum Requirements Comparison
    story.append(Paragraph("1. Curriculum Scope vs. Advanced Tool Capabilities", h2_style))
    scope_data = [
        [Paragraph("Sqrock Prescribed Minimum Requirements", meta_label), Paragraph("Advanced Capabilities Built into Harvester Tool", meta_label)],
        [
            Paragraph("• Write a Python script using regex<br/>• Scrape emails from practice/lab website<br/>• Remove duplicate entries using set()<br/>• Short write-up on attacker exploitation", body_style),
            Paragraph("• <b>Dual Source Engine:</b> Fetches remote HTTP(S) URLs & local offline HTML testbeds<br/>• <b>RFC Email Regex:</b> Handles subdomains, plus-tags, and cleans punctuation artifacts<br/>• <b>Automated Pretexting Engine:</b> Evaluates department risk (Finance, HR, IT Support)<br/>• <b>Threat Vector Mapping:</b> Predicts BEC, malicious CV macros, and credential lures<br/>• <b>Audit Deliverable:</b> Automatically exports structured JSON report to <code>reports/</code>", body_style)
        ]
    ]
    scope_table = Table(scope_data, colWidths=[230, 310])
    scope_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e0f2fe")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#93c5fd")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#bfdbfe")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(scope_table)
    story.append(Spacer(1, 6))

    # 4. Harvested Findings Table
    story.append(Paragraph("2. Harvested Email Intelligence & Threat Vectors", h2_style))
    findings_data = [
        [Paragraph("#", meta_label), Paragraph("Harvested Address", meta_label), Paragraph("Department", meta_label), Paragraph("Risk Level", meta_label), Paragraph("Predicted Attacker Pretext / Threat Vector", meta_label)],
        [Paragraph("1", meta_val), Paragraph("billing-invoices@apexdynamics-lab.local", code_style), Paragraph("Finance", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("Business Email Compromise (BEC): Fake overdue supplier invoice requiring urgent wire transfer.", body_style)],
        [Paragraph("2", meta_val), Paragraph("careers@apexdynamics-lab.local", code_style), Paragraph("HR / Talent", meta_val), Paragraph("<font color='#ea580c'><b>HIGH</b></font>", meta_val), Paragraph("Weaponized Macro Lure: Phishing resume with malicious macro (.docm/.pdf) to gain initial foothold.", body_style)],
        [Paragraph("3", meta_val), Paragraph("finance.desk@apexdynamics-lab.local", code_style), Paragraph("Finance", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("CEO Impersonation Fraud: Spoofed executive directing payroll reroute or confidential gift card scam.", body_style)],
        [Paragraph("4", meta_val), Paragraph("hr-department@apexdynamics-lab.local", code_style), Paragraph("HR", meta_val), Paragraph("<font color='#ea580c'><b>HIGH</b></font>", meta_val), Paragraph("Employee Verification Lure: Inquiring about employee identity to harvest internal employee directory.", body_style)],
        [Paragraph("5", meta_val), Paragraph("info@apexdynamics-lab.local", code_style), Paragraph("General", meta_val), Paragraph("<font color='#0284c7'><b>MEDIUM</b></font>", meta_val), Paragraph("Reconnaissance Pivot: General query to map response timing, auto-responder signatures, and internal mail servers.", body_style)],
        [Paragraph("6", meta_val), Paragraph("it-support@apexdynamics-lab.local", code_style), Paragraph("IT Support", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("Credential Phishing: Cloned SSO login page claiming mandatory MFA certificate renewal.", body_style)],
        [Paragraph("7", meta_val), Paragraph("security-ops@apexdynamics-lab.local", code_style), Paragraph("IT Security", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("Incident Response Spoofing: Alerting users of 'active breach', requesting temporary elevated permissions.", body_style)],
    ]
    findings_table = Table(findings_data, colWidths=[18, 175, 58, 55, 234])
    findings_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(findings_table)
    story.append(Spacer(1, 6))

    # Footer Page 1
    footer_p1 = "<font color='#64748b' size='7.5'><i>Page 1 of 2 — Sqrock IT Solution Alpha 2 Cybersecurity Track • Evaluated Deliverable</i></font>"
    story.append(Paragraph(footer_p1, body_style))

    # ------------------ PAGE 2: Security Analysis & Defenses ------------------
    story.append(PageBreak())

    story.append(Paragraph("3. In-Depth Security Analysis: Pretexting Mechanics", h2_style))
    analysis_text = """
    <b>What is Pretexting?</b> Pretexting is the psychological foundation of social engineering. Unlike brute-force attacks that attack technical vulnerabilities, pretexting attacks human cognitive biases (authority, urgency, scarcity, and trust). By scraping specific departmental email addresses, an adversary eliminates guesswork and custom-tailors an identity that fits the victim's organizational context.<br/><br/>
    <b>Why Address Harvesting Enables Multi-Stage Attacks:</b><br/>
    1. <b>Footprinting Organization Structure:</b> Harvested prefixes (e.g. <code>careers@</code>, <code>billing@</code>) identify existing internal departments, internal naming conventions, and third-party vendors.<br/>
    2. <b>Bypassing Email Gateways:</b> Emails sent to publicly exposed departmental aliases are rarely blocked by spam filters because these addresses are designed to receive external incoming communications.<br/>
    3. <b>Targeting High-Value Roles:</b> Finance employees who process transactions are prioritized for Business Email Compromise (BEC), while HR employees are targeted with weaponized resume attachments.
    """
    story.append(Paragraph(analysis_text, body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("4. Defensive Countermeasures & Engineering Mitigations", h2_style))
    defenses_data = [
        [Paragraph("Defensive Layer", meta_label), Paragraph("Recommended Implementation", meta_label), Paragraph("Effectiveness Against Harvesters", meta_label)],
        [Paragraph("1. Contact Obfuscation", meta_val), Paragraph("Replace plaintext <code>mailto:</code> tags with server-side web contact forms protected by reCAPTCHA v3 or Cloudflare Turnstile.", body_style), Paragraph("Completely prevents automated regex web scrapers from identifying contact addresses.", body_style)],
        [Paragraph("2. Email Authentication", meta_val), Paragraph("Enforce strict <b>SPF (Sender Policy Framework)</b>, <b>DKIM cryptographic signatures</b>, and <b>DMARC policy (p=reject)</b>.", body_style), Paragraph("Prevents external attackers from spoofing legitimate corporate domains in spear-phishing campaigns.", body_style)],
        [Paragraph("3. Email Gateway Sandboxing", meta_val), Paragraph("Deploy Advanced Threat Protection (ATP) solutions (e.g. Proofpoint, Mimecast) with attachment sandboxing and link rewriting.", body_style), Paragraph("Neutralizes weaponized macro attachments sent to HR and analyzes inbound phishing links.", body_style)],
        [Paragraph("4. Out-of-Band Verification", meta_val), Paragraph("Establish mandatory phone verification protocols for any wire transfer or payment change request over $1,000.", body_style), Paragraph("Eliminates wire transfer fraud even if finance addresses are successfully targeted.", body_style)],
    ]
    defenses_table = Table(defenses_data, colWidths=[120, 250, 170])
    defenses_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(defenses_table)
    story.append(Spacer(1, 10))

    story.append(Paragraph("5. Ethical Compliance & Conclusion", h2_style))
    conclusion_text = """
    This laboratory exercise successfully validated the role of automated Python regex tools in passive social engineering preparation. All data collection was conducted exclusively on local, simulated practice assets (<code>lab_target.html</code>) in full compliance with the <b>Indian Information Technology Act, 2000</b> and the <b>US Computer Fraud and Abuse Act (CFAA)</b>. At no point were external, unauthorized, or production systems probed.
    """
    story.append(Paragraph(conclusion_text, body_style))
    story.append(Spacer(1, 10))

    footer_p2 = "<font color='#64748b' size='7.5'><i>Page 2 of 2 — Compiled for Sqrock IT Solution Alpha 2 Cybersecurity Internship • Evaluated Practical Task</i></font>"
    story.append(Paragraph(footer_p2, body_style))

    doc.build(story)
    print(f"[+] Executive PDF Report created successfully at: {output_pdf_path}")

if __name__ == "__main__":
    create_day02_report()
