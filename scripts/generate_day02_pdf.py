"""
Generate Official 3-Page Executive PDF Report for Day 2 Deliverable
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    day02_root = os.path.dirname(script_dir)
    
    if output_pdf_path is None:
        output_pdf_path = os.path.join(day02_root, "reports", "Day02_Email_Harvesting_Report_Sqrock_MdPeerSiddiqui.pdf")
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
    
    primary_color = colors.HexColor("#0f172a")     # Dark slate
    accent_color = colors.HexColor("#0284c7")      # Cyber blue
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
        fontSize=10,
        leading=13,
        textColor=accent_color,
        spaceAfter=5
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=primary_color,
        spaceBefore=7,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=text_dark,
        spaceAfter=4
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=primary_color
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
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

    # ------------------ PAGE 1: Executive Overview & Technical Findings ------------------
    story.append(Paragraph("CYBERSECURITY INTERNSHIP — PRACTICAL LAB REPORT", subtitle_style))
    story.append(Paragraph("Day 02: Email Harvesting & Social Engineering Preparation", title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_color, spaceBefore=2, spaceAfter=6))

    # Metadata Grid
    meta_data = [
        [
            Paragraph("Intern Name:", meta_label), Paragraph("Md Peer Siddiqui", meta_val),
            Paragraph("Program / Track:", meta_label), Paragraph("Alpha 2 — Cybersecurity Track", meta_val)
        ],
        [
            Paragraph("Issuing Body:", meta_label), Paragraph("Sqrock IT Solution", meta_val),
            Paragraph("Date of Execution:", meta_label), Paragraph("October 21–22, 2026", meta_val)
        ],
        [
            Paragraph("Lab Environment:", meta_label), Paragraph("Authorized Local Practice Testbed (lab_target.html)", meta_val),
            Paragraph("GitHub Repository:", meta_label), Paragraph("<font color='#0284c7'><u>github.com/MdPeerSiddiqui/Peer-s-Email-Harvester</u></font>", meta_val)
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
    story.append(Spacer(1, 4))

    # 1. Objective & 2. Tools
    story.append(Paragraph("1. Objective & Scope", h2_style))
    story.append(Paragraph("To extract public-facing email addresses from web documents using Python and regular expressions, and analyze how harvested contacts are weaponized by threat actors to perform organizational profiling and craft high-conviction social engineering pretexts.", body_style))

    story.append(Paragraph("2. Tools and Environment", h2_style))
    story.append(Paragraph("• <b>Environment:</b> Kali Linux 2026.2 (64-bit VirtualBox VM) / Windows 11 Host &bull; <b>Python:</b> 3.11.9 / 3.14.0<br/>• <b>Libraries:</b> <code>requests</code> (v2.34.2 HTTP fetching), <code>re</code> (RFC 5322 regex engine), <code>colorama</code> (v0.4.6 CLI UI styling)<br/>• <b>Target:</b> <code>lab_target.html</code> (Simulated communications directory for <i>Apex Dynamics Inc.</i>)", body_style))
    story.append(Spacer(1, 4))

    # 3. Methodology & 4. Implementation
    story.append(Paragraph("3. Methodology & Implementation", h2_style))
    story.append(Paragraph("1. <b>Content Retrieval:</b> The script reads target HTML content via standard HTTP GET or file streaming.<br/>2. <b>Pattern Matching:</b> Evaluates raw DOM text against RFC regex: <code>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+</code><br/>3. <b>Sanitization & Deduplication:</b> Cleans punctuation artifacts, normalizes to lowercase, and utilizes <code>set()</code> to remove duplicates.<br/>4. <b>Threat Modeling:</b> Automatically maps prefixes to business departments and assigns threat vectors (BEC, macro CV lures).", body_style))
    story.append(Spacer(1, 4))

    # 5. Results & Verification Table
    story.append(Paragraph("4. Results and Verification (7 Unique Addresses Discovered)", h2_style))
    findings_data = [
        [Paragraph("#", meta_label), Paragraph("Harvested Address", meta_label), Paragraph("Department", meta_label), Paragraph("Risk Level", meta_label), Paragraph("Primary Threat Vector / Predicted Pretext", meta_label)],
        [Paragraph("1", meta_val), Paragraph("billing-invoices@apexdynamics-lab.local", code_style), Paragraph("Finance", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("Business Email Compromise (BEC): Fake overdue supplier invoice wire transfer.", body_style)],
        [Paragraph("2", meta_val), Paragraph("careers@apexdynamics-lab.local", code_style), Paragraph("HR / Talent", meta_val), Paragraph("<font color='#ea580c'><b>HIGH</b></font>", meta_val), Paragraph("Weaponized Macro Lure: Phishing resume with malicious macro (.docm/.pdf).", body_style)],
        [Paragraph("3", meta_val), Paragraph("finance.desk@apexdynamics-lab.local", code_style), Paragraph("Finance", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("CEO Impersonation Fraud: Spoofed executive directing payroll reroute.", body_style)],
        [Paragraph("4", meta_val), Paragraph("hr-department@apexdynamics-lab.local", code_style), Paragraph("HR", meta_val), Paragraph("<font color='#ea580c'><b>HIGH</b></font>", meta_val), Paragraph("Employee Verification Lure: Harvesting internal employee directory details.", body_style)],
        [Paragraph("5", meta_val), Paragraph("info@apexdynamics-lab.local", code_style), Paragraph("General", meta_val), Paragraph("<font color='#0284c7'><b>MEDIUM</b></font>", meta_val), Paragraph("Reconnaissance Pivot: Mapping mail server signatures and employee hierarchy.", body_style)],
        [Paragraph("6", meta_val), Paragraph("it-support@apexdynamics-lab.local", code_style), Paragraph("IT Support", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("Credential Phishing: Cloned SSO login claiming mandatory MFA certificate renewal.", body_style)],
        [Paragraph("7", meta_val), Paragraph("security-ops@apexdynamics-lab.local", code_style), Paragraph("IT Security", meta_val), Paragraph("<font color='#dc2626'><b>CRITICAL</b></font>", meta_val), Paragraph("Incident Response Spoofing: Alerting users of active breach to request elevated access.", body_style)],
    ]
    findings_table = Table(findings_data, colWidths=[18, 175, 58, 55, 234])
    findings_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(findings_table)
    story.append(Spacer(1, 6))

    footer_p1 = "<font color='#64748b' size='7'><i>Page 1 of 3 — Sqrock IT Solution Alpha 2 Cybersecurity Track • Evaluated Deliverable</i></font>"
    story.append(Paragraph(footer_p1, body_style))

    # ------------------ PAGE 2: Security Analysis & Defenses ------------------
    story.append(PageBreak())

    story.append(Paragraph("5. Security Analysis: Potential Misuse & Attack Vectors", h2_style))
    analysis_text = """
    <b>Why Harvested Emails are High-Conviction Threat Vectors:</b><br/>
    • <b>Targeted Spear-Phishing:</b> Unlike bulk spam, scraped departmental addresses enable attackers to craft highly targeted messages. An attacker emailing <code>careers@</code> knows the recipient expects resumes from strangers, significantly increasing click rates for weaponized documents.<br/>
    • <b>Business Email Compromise (BEC):</b> Harvesting <code>billing-invoices@</code> enables adversaries to monitor supplier cycles and issue fraudulent payment redirection instructions.<br/>
    • <b>Organizational Footprinting:</b> Public contact formats reveal internal user ID structures and third-party SaaS vendors.<br/>
    • <b>Absence of Consent:</b> Public visibility does not imply consent to receive deceptive or spoofed communications.
    """
    story.append(Paragraph(analysis_text, body_style))
    story.append(Spacer(1, 6))

    story.append(Paragraph("6. Defensive Countermeasures & Engineering Mitigations", h2_style))
    defenses_data = [
        [Paragraph("Defensive Layer", meta_label), Paragraph("Recommended Implementation", meta_label), Paragraph("Effectiveness Against Harvesters", meta_label)],
        [Paragraph("1. Contact Obfuscation", meta_val), Paragraph("Replace plaintext <code>mailto:</code> tags with server-side web contact forms protected by reCAPTCHA v3 or Cloudflare Turnstile.", body_style), Paragraph("Completely prevents automated regex web scrapers from identifying contact addresses.", body_style)],
        [Paragraph("2. Email Authentication", meta_val), Paragraph("Enforce strict <b>SPF (Sender Policy Framework)</b>, <b>DKIM cryptographic signatures</b>, and <b>DMARC policy (p=reject)</b>.", body_style), Paragraph("Prevents external attackers from spoofing legitimate corporate domains in spear-phishing campaigns.", body_style)],
        [Paragraph("3. Email Gateway Sandboxing", meta_val), Paragraph("Deploy Advanced Threat Protection (ATP) solutions (e.g. Proofpoint, Mimecast) with attachment sandboxing and link rewriting.", body_style), Paragraph("Neutralizes weaponized macro attachments sent to HR and analyzes inbound phishing links.", body_style)],
        [Paragraph("4. Out-of-Band Verification", meta_val), Paragraph("Establish mandatory phone verification protocols for any wire transfer or payment change request over $1,000.", body_style), Paragraph("Eliminates wire transfer fraud even if finance addresses are successfully targeted.", body_style)],
    ]
    defenses_table = Table(defenses_data, colWidths=[110, 250, 180])
    defenses_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(defenses_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("7. Ethical Compliance & Conclusion", h2_style))
    conclusion_text = """
    <b>Ethical Scope:</b> All testing was conducted strictly on local simulation assets (<code>lab_target.html</code>) in compliance with the Indian Information Technology Act, 2000 (Section 43 & 66) and the US Computer Fraud and Abuse Act (CFAA). No unauthorized systems were probed.<br/>
    <b>Conclusion:</b> This exercise demonstrated how simple regex automation exposes an organization's public contact hierarchy and enables multi-stage social engineering. Defense requires combining technical measures (DMARC p=reject, form obfuscation) with strict employee verification policies.
    """
    story.append(Paragraph(conclusion_text, body_style))
    story.append(Spacer(1, 6))

    footer_p2 = "<font color='#64748b' size='7'><i>Page 2 of 3 — Compiled for Sqrock IT Solution Alpha 2 Cybersecurity Track • Evaluated Deliverable</i></font>"
    story.append(Paragraph(footer_p2, body_style))

    # ------------------ PAGE 3: Practical Execution Proof (Screenshots) ------------------
    story.append(PageBreak())

    story.append(Paragraph("8. Appendix: Practical Execution Proof (Kali Linux 2026)", h2_style))
    story.append(Paragraph("The following screenshots verify live execution of PEER'S Email Harvester inside Kali Linux, including Git cloning from GitHub, ASCII banner initialization, and full pretexting analysis:", body_style))
    story.append(Spacer(1, 4))

    img1 = os.path.join(day02_root, "screenshots", "day02_kali_clone_banner.png")
    img2 = os.path.join(day02_root, "screenshots", "day02_kali_exec_part1.png")
    img3 = os.path.join(day02_root, "screenshots", "day02_kali_exec_part2.png")

    if os.path.exists(img1):
        story.append(Image(img1, width=540, height=145))
        story.append(Spacer(1, 4))
    if os.path.exists(img2):
        story.append(Image(img2, width=540, height=135))
        story.append(Spacer(1, 4))
    if os.path.exists(img3):
        story.append(Image(img3, width=540, height=135))
        story.append(Spacer(1, 4))

    footer_p3 = "<font color='#64748b' size='7'><i>Page 3 of 3 — GitHub Repository: https://github.com/MdPeerSiddiqui/Peer-s-Email-Harvester</i></font>"
    story.append(Paragraph(footer_p3, body_style))

    doc.build(story)
    print(f"[+] Official 3-Page PDF Report compiled successfully at: {output_pdf_path}")

if __name__ == "__main__":
    create_day02_report()
