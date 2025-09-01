section_html_templates = {
    # This section matches the header in the example HTML template.
    "Header": """
    <div class="case-header">
        <div class="case-number"><strong>AAA Case No.: [To be Assigned]</strong></div>
        
        <div class="parties">
            <strong>Erika Gomez,</strong> <strong>Claimant,</strong><br><br>
            <strong>v.</strong><br><br>
            <strong>MIDLAND FUNDING LLC, and</strong> <strong>MIDLAND CREDIT MANAGEMENT, INC.,</strong><br>
            <strong>Respondents.</strong>
        </div>
        
        <div class="document-title">ARBITRATION COMPLAINT</div>
    </div>
""",
    # This is a new introductory paragraph that appears before the main sections.
    "Initial Complaint Introduction": """
    <div class="paragraph">
        Claimant Erika Gomez ("Claimant"), by and through her attorneys, as and for her complaint against Respondents MIDLAND FUNDING LLC and MIDLAND CREDIT MANAGEMENT, INC. (hereinafter collectively "Midland") alleges as follows:
    </div>
""",
    # This is a new section based on the example HTML.
    "Introduction": """
    <div class="section-header">INTRODUCTION</div>

    <div class="paragraph">
        <span class="paragraph-number">1.</span> This is an action for actual, statutory, and punitive damages for Respondents' violations of the Fair Debt Collection Practices Act, 15 U.S.C. § 1692, et seq. ("FDCPA"); the Fair Credit Reporting Act, 15 U.S.C. § 1681, et seq. ("FCRA"); the California Rosenthal Fair Debt Collection Practices Act, Cal. Civ. Code § 1788 et seq. ("RFDCPA"); the California Consumer Credit Reporting Agencies Act, Cal. Civ. Code § 1785.1 et seq. ("CCRAA"); and the common law tort of Invasion of Privacy.
    </div>
""",
    # This is a new section, replacing the former "Jurisdiction and Arbitrability" with new content and formatting.
    "Basis for Arbitration": """
    <div class="section-header">BASIS FOR ARBITRATION</div>

    <div class="paragraph">
        <span class="paragraph-number">2.</span> Upon information and belief, the alleged financial obligation originated from a Milestone Mastercard account issued by The Bank of Missouri.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">3.</span> The Milestone Mastercard Cardholder Agreement ("the Agreement") governing the account contains a binding arbitration provision. The Agreement mandates that any "Claim" arising out of or related to the Agreement or the account, whether based on statute, contract, or tort, must be resolved by binding arbitration under the Federal Arbitration Act ("FAA"). The Agreement further specifies that the arbitration will be administered by the American Arbitration Association (the "AAA").
    </div>

    <div class="paragraph">
        <span class="paragraph-number">4.</span> Respondents, as alleged subsequent owners and servicers of the account, are bound by the terms of the Agreement, including the Arbitration of Disputes Provision, under the doctrine of equitable estoppel.
    </div>
""",
    # This is a new section from the example HTML.
    "Choice of Law": """
    <div class="section-header">CHOICE OF LAW</div>

    <div class="paragraph">
        <span class="paragraph-number">5.</span> While the Agreement contains a Missouri choice-of-law provision, the wrongful acts giving rise to this action occurred in California. Respondents' tortious and unlawful conduct was directed at a California resident and the injuries were sustained by Claimant in California. As such, California's substantive laws, including its consumer protection statutes and common law, govern Respondents' conduct.
    </div>
""",
    # This section replaces "Party Designation" and "Allegations as to Parties", matching the new content and structure.
    "Parties": """
    <div class="section-header">PARTIES</div>

    <div class="paragraph">
        <span class="paragraph-number">6.</span> Claimant, Erika Gomez, is a natural person residing in the State of California. Claimant is a: a. "consumer" as that term is defined by the Fair Debt Collection Practices Act (FDCPA), <span class="statute-ref">15 U.S.C. § 1692a(3)</span>, meaning a natural person allegedly obligated to pay a debt; and a b. "debtor" as that term is defined by the Rosenthal Fair Debt Collection Practices Act (RFDCPA), <span class="statute-ref">Cal. Civ. Code § 1788.2(h)</span>, meaning a natural person from whom a debt collector seeks to collect a consumer debt. c. "consumer" as that term is defined by the Fair Credit Reporting Act (FCRA), <span class="statute-ref">15 U.S.C. § 1681a(c)</span>, and the California Consumer Credit Reporting Agencies Act (CCRAA), <span class="statute-ref">Cal. Civ. Code § 1785.3(b)</span>, meaning a natural individual.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">7.</span> Upon information and belief, Respondent Midland Funding LLC is a Delaware limited liability company whose principal business purpose is the purchase of defaulted consumer debts.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">8.</span> Upon information and belief, Respondents are "debt collectors" as defined by the FDCPA, <span class="statute-ref">15 U.S.C. § 1692a(6)</span>, in that their principal purpose is the collection of debts and they regularly attempt to collect, directly or indirectly, debts owed or due another. They are also "debt collectors" under the RFDCPA, <span class="statute-ref">Cal. Civ. Code § 1788.2(c)</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">9.</span> By obtaining Claimant's consumer credit reports, Respondents also acted as "users of a consumer credit report" as defined by the CCRAA, <span class="statute-ref">Cal. Civ. Code § 1785.3(l)</span>, and are subject to the duties of users under the FCRA.
    </div>
""",
    # This section replaces "Factual Summary" and the old "Factual Allegations" with updated content and formatting.
    "Factual Allegations": """
    <div class="section-header">FACTUAL ALLEGATIONS</div>

    <div class="paragraph">
        <span class="paragraph-number">10.</span> Claimant adopts and realleges the foregoing as fully restated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">11.</span> Prior to the commencement of this action, Claimant allegedly incurred a financial obligation under the Milestone Mastercard account that was primarily for personal, family, or household purposes and is therefore a "debt" as defined by <span class="statute-ref">15 U.S.C. § 1692a(5)</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">12.</span> Sometime thereafter, the alleged debt was transferred to or placed with Respondents for collection from the Claimant.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">13.</span> On or about January 10, 2025, Claimant sent a written notice to Midland informing Respondents that the only convenient and acceptable method of communication was via email and provided her email address.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">14.</span> The notice was delivered to Midland on or about January 14, 2025, putting Respondents on notice that communicating via postal mail was inconvenient and impermissible.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">15.</span> Despite Claimant's instructions, Midland sent Claimant a collection letter dated January 21, 2025, via postal mail. This was a "communication" in an attempt to collect a debt as that term is defined by <span class="statute-ref">15 U.S.C. § 1692a(2)</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">16.</span> Separately, upon information and belief, Midland obtained Claimant's TransUnion credit report without a permissible purpose on at least six occasions, on or about the following dates: January 9, 2024; November 10, 2023; September 6, 2023; July 22, 2023; May 5, 2023; and March 3, 2023.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">17.</span> In light of the facts articulated herein, Respondents contacted the Claimant at a place and in a manner they knew was inconvenient; engaged in conduct the natural consequence of which was to harass and oppress the Claimant; and used unfair, unconscionable, and deceptive means to collect a debt.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">18.</span> Claimant suffered actual damages, including stress, anxiety, humiliation, invasion of privacy, financial costs for credit monitoring, and loss of productive time.
    </div>
""",
    # This is a new section, replacing the former "Practices of the Respondent" with new content and formatting.
    "Allegations of Law": """
    <div class="section-header">ALLEGATIONS OF LAW</div>

    <div class="paragraph">
        <span class="paragraph-number">19.</span> Respondents' conduct violated numerous provisions of the FDCPA, including but not limited to <span class="statute-ref">15 U.S.C. §§ 1692c(a)(1), 1692d, 1692e(10), and 1692f</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">20.</span> Respondents' conduct violated the FCRA, including but not limited to <span class="statute-ref">15 U.S.C. § 1681b(f)</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">21.</span> Respondents' conduct violated the RFDCPA, including but not limited to <span class="statute-ref">Cal. Civ. Code §§ 1788.14 and 1788.17</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">22.</span> Respondents' conduct violated the CCRAA, including but not limited to <span class="statute-ref">Cal. Civ. Code § 1785.19</span>.
    </div>
""",
    # This section consolidates and refactors the "Causes of Action" heavily to match the template's structure.
    "Causes of Action": """
    <div class="section-header">CAUSES OF ACTION</div>

    <div class="count-header"><strong>COUNT I: Violations of the Fair Debt Collection Practices Act (FDCPA)</strong></div>

    <div class="paragraph">
        <span class="paragraph-number">11.</span> Claimant adopts and realleges the foregoing as fully stated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">12.</span> At all relevant times, Claimant was a "consumer", the alleged obligation was a "debt", and Respondents were acting as "debt collectors", bringing their conduct under the purview of the FDCPA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">13.</span> Respondents violated multiple provisions of the FDCPA, including but not limited to:
    </div>

    <div class="bullet-point">
        <strong><span class="statute-ref">15 U.S.C. § 1692c(a)(1)</span> -- Communication at an Inconvenient Place:</strong> Respondents communicated with the Claimant by sending a collection letter via postal mail after Claimant provided clear written instructions to only use email, making the mail communication to a place and in a manner known to be inconvenient.
    </div>

    <div class="bullet-point">
        <strong><span class="statute-ref">15 U.S.C. § 1692e(10)</span> -- Deceptive Means:</strong> Respondents used deceptive means to obtain information concerning a consumer by accessing Claimant's credit reports on multiple occasions, thereby falsely representing that they had a permissible purpose and legal right to do so.
    </div>

    <div class="bullet-point">
        <strong><span class="statute-ref">15 U.S.C. § 1692f</span> -- Unfair or Unconscionable Means:</strong> Respondents used unfair and unconscionable means to attempt to collect a debt by obtaining Claimant's private financial information from credit reporting agencies without authorization or a legitimate purpose.
    </div>

    <div class="bullet-point">
        <strong><span class="statute-ref">15 U.S.C. § 1692d</span> -- Harassment or Oppression:</strong> Respondents engaged in conduct the natural consequence of which was to harass and oppress the Claimant by willfully ignoring her written instructions regarding communication, a method intended to protect her privacy and peace of mind.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">14.</span> As a direct and proximate result of Respondents' violations, Claimant suffered actual damages, including but not limited to, emotional distress, anxiety, invasion of privacy, financial costs for credit monitoring, and the loss of productive time spent investigating and addressing the unlawful conduct.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">15.</span> Pursuant to <span class="statute-ref">15 U.S.C. § 1692k</span>, Respondents are liable to Claimant for her actual damages, statutory damages of $1,000, and the costs of this action, including reasonable attorney's fees.
    </div>

    <div class="count-header"><strong>COUNT II: Violations of the Fair Credit Reporting Act (FCRA)</strong></div>

    <div class="paragraph">
        <span class="paragraph-number">16.</span> Claimant adopts and realleges the foregoing as fully stated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">17.</span> At all relevant times, Claimant was a "consumer", the credit reports at issue were "consumer reports," and Respondents were "users" of those reports, subjecting their conduct to the requirements of the FCRA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">18.</span> Respondents violated <span class="statute-ref">15 U.S.C. § 1681b(f)</span> by using or obtaining Claimant's consumer reports on at least six occasions without a permissible purpose. As alleged above, Claimant never provided written authorization for these inquiries and had no established relationship with or pending transaction initiated by Claimant that would provide Respondents with a permissible purpose under any provision of <span class="statute-ref">15 U.S.C. § 1681b</span>.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">19.</span> Respondents' violations of the FCRA were willful. Respondents, as sophisticated national debt collectors, know or should know the strict limitations on accessing consumer reports. By repeatedly obtaining Claimant's reports without a permissible purpose, Respondents acted with knowing or reckless disregard for their statutory duties under the FCRA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">20.</span> As a direct and proximate result of Respondents' willful violations, Claimant suffered actual damages, including emotional distress, invasion of privacy, financial costs for credit monitoring, and lost time.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">21.</span> Pursuant to <span class="statute-ref">15 U.S.C. § 1681n</span>, for their willful noncompliance, Respondents are liable to Claimant for her actual damages, statutory damages of $1,000 for each violation, punitive damages as the Arbitrator may allow, and the costs of this action, including reasonable attorney's fees.
    </div>

    <div class="count-header"><strong>COUNT III: Violations of the Rosenthal Fair Debt Collection Practices Act (RFDCPA)</strong></div>

    <div class="paragraph">
        <span class="paragraph-number">22.</span> Claimant adopts and realleges the foregoing as fully stated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">23.</span> At all relevant times, Claimant was a "debtor" (<span class="statute-ref">Cal. Civ. Code § 1788.2(h)</span>), the obligation was a "consumer debt" (<span class="statute-ref">§ 1788.2(f)</span>), and Respondents were "debt collectors" (<span class="statute-ref">§ 1788.2(c)</span>) collecting a consumer debt, making their conduct subject to the RFDCPA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">24.</span> Respondents violated multiple provisions of the RFDCPA, including but not limited to:
    </div>

    <div class="bullet-point">
        <strong><span class="statute-ref">California Civil Code § 1788.14(c)</span>:</strong> Respondents initiated communication with the Claimant by mail after the Claimant provided written instructions to use a different method of communication (email).
    </div>

    <div class="bullet-point">
        <strong><span class="statute-ref">California Civil Code § 1788.17</span>:</strong> Respondents failed to comply with the provisions of the federal FDCPA (specifically <span class="statute-ref">15 U.S.C. §§ 1692c, 1692d, 1692e, and 1692f</span>), which constitutes a direct violation of the RFDCPA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">25.</span> Respondents' disregard for Claimant's clear, written instructions and for the plain language of the statutes constituted a knowing and willful violation of California law.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">26.</span> As a direct result of these violations, Claimant suffered actual damages.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">27.</span> Pursuant to <span class="statute-ref">California Civil Code § 1788.30</span>, Respondents are liable to Claimant for her actual damages, a statutory penalty of $1,000, and the costs of this action, including reasonable attorney's fees.
    </div>

    <div class="count-header"><strong>COUNT IV: Violations of the California Consumer Credit Reporting Agencies Act (CCRAA)</strong></div>

    <div class="paragraph">
        <span class="paragraph-number">28.</span> Claimant adopts and realleges the foregoing as fully stated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">29.</span> At all relevant times, Claimant was a "consumer" (<span class="statute-ref">Cal. Civ. Code § 1785.3(b)</span>), the reports at issue were "consumer credit reports" (<span class="statute-ref">§ 1785.3(c)</span>), and Respondents were "users of a consumer credit report" (<span class="statute-ref">§ 1785.3(l)</span>), subjecting their conduct to the requirements of the CCRAA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">30.</span> Respondents violated <span class="statute-ref">California Civil Code § 1785.19(a)</span> by obtaining and using Claimant's consumer credit reports on at least six occasions for a purpose other than a purpose for which the report may be furnished under Section 1785.11.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">31.</span> Respondents' violations of the CCRAA were willful. As one of the largest and most sophisticated debt purchasers in the nation, Respondents know, or are reckless in not knowing, the strict legal requirements for accessing consumer credit reports. The pattern of obtaining Claimant's report on six separate occasions, without any transaction initiated by the Claimant or any authorization, demonstrates a knowing and intentional violation of the CCRAA, or at a minimum, a reckless disregard for the Claimant's statutory rights. This conduct was not the result of an isolated error but rather reflects a deliberate business practice.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">32.</span> As a direct result of these willful violations, Claimant suffered actual damages.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">33.</span> Respondents' willful violations of the CCRAA render them liable to Claimant for her actual damages and justify the imposition of punitive damages of $5,000 for each of the six willful violations in order to punish their conduct and deter future misconduct, in addition to the costs of this action and reasonable attorney's fees, pursuant to <span class="statute-ref">California Civil Code § 1785.31</span>.
    </div>

    <div class="count-header"><strong>COUNT V: Invasion of Privacy -- Intrusion Upon Seclusion</strong></div>

    <div class="paragraph">
        <span class="paragraph-number">34.</span> Claimant adopts and realleges the foregoing as fully stated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">35.</span> Claimant possessed a reasonable expectation of privacy in her sensitive personal and financial information contained within her consumer credit reports and in her right to be free from unwanted communications at her home.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">36.</span> Respondents intentionally intruded upon Claimant's seclusion by engaging in a tactical and calculative practice of systematically accessing her private credit reports. This intrusion was not only to collect an alleged debt but also, upon information and belief, to survey and harvest other private data related to the Claimant, all without authorization or legal justification.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">37.</span> Respondents' conduct is highly offensive to a reasonable person. The intrusion was not an accident but a deliberate tactic employed to oppress the Claimant and force payment of the alleged debt. Such calculated disregard for a consumer's privacy by a sophisticated debt collector is extreme and outrageous.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">38.</span> As a direct and proximate result of this intrusion, Claimant suffered harm, including but not limited to, mental anguish, frustration, and emotional distress.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">39.</span> Respondents' conduct, as part of a business practice designed to leverage private information and coerce consumers, was willful, malicious, and oppressive. This conscious disregard for Claimant's fundamental right to privacy was not only unauthorized by law but was a calculated strategy, justifying the imposition of punitive damages to punish and deter such behavior.
    </div>
""",
    # This section is refactored to match the example HTML's content and structure.
    "Prayer for Relief": """
    <div class="prayer-section">
        <div class="section-header">PRAYER FOR RELIEF</div>
        
        <div class="paragraph">
            Claimant, Erika Gomez, prays that the Arbitrator enter an award in her favor and against Respondents, granting the following relief:
        </div>

        <div class="paragraph">
            a. <strong>Actual and Compensatory Damages</strong> in an amount to be determined at arbitration for Claimant's emotional distress, financial expenses, and loss of productive time;
        </div>

        <div class="paragraph">
            b. <strong>Statutory Damages</strong> under federal law, including: i. $1,000 for violations of the FDCPA, pursuant to <span class="statute-ref">15 U.S.C. § 1692k</span>; and ii. $1,000 for each of the six willful violations of the FCRA, pursuant to <span class="statute-ref">15 U.S.C. § 1681n</span>.
        </div>

        <div class="paragraph">
            c. <strong>A Statutory Penalty</strong> of $1,000 for violations of California's RFDCPA, pursuant to <span class="statute-ref">Cal. Civ. Code § 1788.30</span>;
        </div>

        <div class="paragraph">
            d. <strong>Punitive Damages for Willful Violations of the CCRAA</strong>, specifically $5,000 for each of the six instances where Respondents willfully obtained Claimant's credit report without a permissible purpose, in order to punish their unlawful conduct and to deter them from engaging in such misconduct in the future, pursuant to <span class="statute-ref">Cal. Civ. Code § 1785.31</span>;
        </div>

        <div class="paragraph">
            e. <strong>Punitive Damages for Willful Violations of the FCRA and Common Law</strong>, in an amount to be determined at arbitration, sufficient to punish and deter Respondents' malicious and oppressive conduct;
        </div>

        <div class="paragraph">
            f. <strong>Costs and Attorneys' Fees</strong> incurred in prosecuting this action, as provided by the FDCPA, FCRA, RFDCPA, and CCRAA; and
        </div>

        <div class="paragraph">
            g. <strong>Such other and further relief</strong> as the Arbitrator deems just and proper.
        </div>
    </div>
""",
    # This section is refactored to exactly match the example HTML's content and structure, removing placeholders.
    "Signature Block": """
    <div class="signature-block">
        <p>Respectfully submitted,</p>
        
        <p>Dated: June 9, 2025</p>
        
        <div class="signature-line">
            <p>By: /s/ Rachel Rodriguez</p>
            
            <p>Rachel Rodriguez, Esq.<br>
            Paragon Law Group, PLLC<br>
            712 H Street NE, Suite 1724<br>
            Washington, DC 20002<br>
            Tel: (866) 560-0666<br>
            Email: rrodriguez@paragonlawgroup.net</p>
            
            <p><em>Attorney for Claimant Erika Gomez</em></p>
        </div>
    </div>
""",
}

from gpt_section_generator import llm
# import pdfkit
import os
from datetime import datetime
# from fpdf import FPDF
from weasyprint import HTML


# path_to_wkhtmltopdf = r'wkhtmltopdf.exe'

# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arbitration Complaint - Gomez v. Midland Funding LLC</title>
    <style>
        body {
            font-family: 'Times New Roman', Times, serif;
            line-height: 1.6;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 1in;
            background-color: #fff;
            color: #000;
        }
        .case-header {
            text-align: center;
            margin-bottom: 2em;
        }
        .case-number {
            font-weight: bold;
            margin-bottom: 1em;
        }
        .parties {
            font-weight: bold;
            text-align: center;
            margin-bottom: 1em;
        }
        .document-title {
            font-weight: bold;
            text-align: center;
            text-decoration: underline;
            font-size: 1.1em;
            margin-bottom: 2em;
        }
        .section-header {
            font-weight: bold;
            text-align: center;
            margin: 2em 0 1em 0;
            text-decoration: underline;
        }
        .count-header {
            font-weight: bold;
            text-align: center;
            margin: 2em 0 1em 0;
        }
        .paragraph {
            margin-bottom: 1em;
            text-align: justify;
        }
        .paragraph-number {
            display: inline;
            margin-right: 0.5em;
        }
        .statute-ref {
            font-weight: bold;
        }
        .bullet-point {
            margin-left: 2em;
            margin-bottom: 0.5em;
        }
        .prayer-section {
            margin-top: 2em;
            border-top: 1px solid #000;
            padding-top: 1em;
        }
        .signature-block {
            margin-top: 3em;
        }
        .signature-line {
            margin-top: 2em;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin-bottom: 0.5em;
        }
    </style>
</head>
<body>
"""
    
footer = """
</body>
</html>"""

def generate_section_html(section_name, section, previous_sections):
    

    prompt = f"""
    ROLE: You are an expert HTML formatter specializing in legal document structures for AAA arbitration complaints.

    TASK: Convert the provided `INPUT_TEXT` into a well-formed HTML section.

    INSTRUCTIONS:
    1.  **Analyze the `HTML_STRUCTURE_EXAMPLE`**: Carefully examine the provided example for its heading hierarchy (h2, h3), paragraph usage (p), and list structures (ol, ul, li).
    2.  **Apply to `INPUT_TEXT`**: Format the `INPUT_TEXT` using the *same structural patterns* and HTML tags as observed in the `HTML_STRUCTURE_EXAMPLE`. Ensure all content from `INPUT_TEXT` is fully represented and correctly nested within appropriate HTML tags.
    3.  **Maintain Consistency**: The final output HTML should look structurally similar to the example, but with the content replaced by `INPUT_TEXT`.
    4.  **Output Format**: Provide only the complete, well-formed HTML for the section. Do not include any extra commentary, explanations, or markdown fences (```html).
    5.  **Numbering and Continuity**: Use `PREVIOUS_SECTIONS` to maintain correct numbering, section counts, or clause numbering continuity. If the `HTML_STRUCTURE_EXAMPLE` includes specific numbering formats (e.g., "Count I", "Section 3.2"), follow the same style in this output.


    ---
    INPUT_TEXT:
    {section}

    ---
    HTML_STRUCTURE_EXAMPLE (for section '{section_name}'):
    {section_html_templates.get(section_name, "")}
    
    
    ---
    PREVIOUS_SECTIONS (just for numbering consistentencies):
    {previous_sections}
    """

    response = llm(prompt)

    return response.replace('```html', '').replace('```', '').strip()


def generate_pdf_file(html_sections):
    
    html_content = '\n'.join(html_sections)
    
    html_content = header + '\n' + html_content + '\n' + footer
    
    pdf_file_path = f"pdf_generated_files/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

     # Save debug HTML for troubleshooting
    with open("debug_output.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Saved debug_output.html — check it for malformed HTML!")

    # ✅ Add this options block
    options = {
        "enable-local-file-access": "",  # Required for wkhtmltopdf to access local styles/scripts
        "quiet": ""  # Optional: makes output cleaner
    }

    # ✅ Pass options to pdfkit
    # pdfkit.from_string(html_content, pdf_file_path, configuration=config, options=options)
    HTML(string=html_content).write_pdf(pdf_file_path)
    return pdf_file_path