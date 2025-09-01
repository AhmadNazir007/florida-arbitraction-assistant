from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime
from fpdf import FPDF
from weasyprint import HTML

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# path_to_wkhtmltopdf = r'wkhtmltopdf.exe'

# config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)



html_template = """
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

    <div class="paragraph">
        Claimant Erika Gomez ("Claimant"), by and through her attorneys, as and for her complaint against Respondents MIDLAND FUNDING LLC and MIDLAND CREDIT MANAGEMENT, INC. (hereinafter collectively "Midland") alleges as follows:
    </div>

    <div class="section-header">INTRODUCTION</div>

    <div class="paragraph">
        <span class="paragraph-number">1.</span> This is an action for actual, statutory, and punitive damages for Respondents' violations of the Fair Debt Collection Practices Act, 15 U.S.C. § 1692, et seq. ("FDCPA"); the Fair Credit Reporting Act, 15 U.S.C. § 1681, et seq. ("FCRA"); the California Rosenthal Fair Debt Collection Practices Act, Cal. Civ. Code § 1788 et seq. ("RFDCPA"); the California Consumer Credit Reporting Agencies Act, Cal. Civ. Code § 1785.1 et seq. ("CCRAA"); and the common law tort of Invasion of Privacy.
    </div>

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

    <div class="section-header">CHOICE OF LAW</div>

    <div class="paragraph">
        <span class="paragraph-number">5.</span> While the Agreement contains a Missouri choice-of-law provision, the wrongful acts giving rise to this action occurred in California. Respondents' tortious and unlawful conduct was directed at a California resident and the injuries were sustained by Claimant in California. As such, California's substantive laws, including its consumer protection statutes and common law, govern Respondents' conduct.
    </div>

    <div class="section-header">PARTIES</div>

    <div class="paragraph">
        <span class="paragraph-number">6.</span> Claimant, Erika Gomez, is a natural person residing in the State of California. Claimant is a: a. "consumer" as that term is defined by the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692a(3), meaning a natural person allegedly obligated to pay a debt; and a b. "debtor" as that term is defined by the Rosenthal Fair Debt Collection Practices Act (RFDCPA), Cal. Civ. Code § 1788.2(h), meaning a natural person from whom a debt collector seeks to collect a consumer debt. c. "consumer" as that term is defined by the Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681a(c), and the California Consumer Credit Reporting Agencies Act (CCRAA), Cal. Civ. Code § 1785.3(b), meaning a natural individual.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">7.</span> Upon information and belief, Respondent Midland Funding LLC is a Delaware limited liability company whose principal business purpose is the purchase of defaulted consumer debts.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">8.</span> Upon information and belief, Respondents are "debt collectors" as defined by the FDCPA, 15 U.S.C. § 1692a(6), in that their principal purpose is the collection of debts and they regularly attempt to collect, directly or indirectly, debts owed or due another. They are also "debt collectors" under the RFDCPA, Cal. Civ. Code § 1788.2(c).
    </div>

    <div class="paragraph">
        <span class="paragraph-number">9.</span> By obtaining Claimant's consumer credit reports, Respondents also acted as "users of a consumer credit report" as defined by the CCRAA, Cal. Civ. Code § 1785.3(l), and are subject to the duties of users under the FCRA.
    </div>

    <div class="section-header">FACTUAL ALLEGATIONS</div>

    <div class="paragraph">
        <span class="paragraph-number">10.</span> Claimant adopts and realleges the foregoing as fully restated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">11.</span> Prior to the commencement of this action, Claimant allegedly incurred a financial obligation under the Milestone Mastercard account that was primarily for personal, family, or household purposes and is therefore a "debt" as defined by 15 U.S.C. § 1692a(5).
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
        <span class="paragraph-number">15.</span> Despite Claimant's instructions, Midland sent Claimant a collection letter dated January 21, 2025, via postal mail. This was a "communication" in an attempt to collect a debt as that term is defined by 15 U.S.C. § 1692a(2).
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

    <div class="section-header">ALLEGATIONS OF LAW</div>

    <div class="paragraph">
        <span class="paragraph-number">19.</span> Respondents' conduct violated numerous provisions of the FDCPA, including but not limited to 15 U.S.C. §§ 1692c(a)(1), 1692d, 1692e(10), and 1692f.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">20.</span> Respondents' conduct violated the FCRA, including but not limited to 15 U.S.C. § 1681b(f).
    </div>

    <div class="paragraph">
        <span class="paragraph-number">21.</span> Respondents' conduct violated the RFDCPA, including but not limited to Cal. Civ. Code §§ 1788.14 and 1788.17.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">22.</span> Respondents' conduct violated the CCRAA, including but not limited to Cal. Civ. Code § 1785.19.
    </div>

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
        <strong>15 U.S.C. § 1692c(a)(1) -- Communication at an Inconvenient Place:</strong> Respondents communicated with the Claimant by sending a collection letter via postal mail after Claimant provided clear written instructions to only use email, making the mail communication to a place and in a manner known to be inconvenient.
    </div>

    <div class="bullet-point">
        <strong>15 U.S.C. § 1692e(10) -- Deceptive Means:</strong> Respondents used deceptive means to obtain information concerning a consumer by accessing Claimant's credit reports on multiple occasions, thereby falsely representing that they had a permissible purpose and legal right to do so.
    </div>

    <div class="bullet-point">
        <strong>15 U.S.C. § 1692f -- Unfair or Unconscionable Means:</strong> Respondents used unfair and unconscionable means to attempt to collect a debt by obtaining Claimant's private financial information from credit reporting agencies without authorization or a legitimate purpose.
    </div>

    <div class="bullet-point">
        <strong>15 U.S.C. § 1692d -- Harassment or Oppression:</strong> Respondents engaged in conduct the natural consequence of which was to harass and oppress the Claimant by willfully ignoring her written instructions regarding communication, a method intended to protect her privacy and peace of mind.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">14.</span> As a direct and proximate result of Respondents' violations, Claimant suffered actual damages, including but not limited to, emotional distress, anxiety, invasion of privacy, financial costs for credit monitoring, and the loss of productive time spent investigating and addressing the unlawful conduct.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">15.</span> Pursuant to 15 U.S.C. § 1692k, Respondents are liable to Claimant for her actual damages, statutory damages of $1,000, and the costs of this action, including reasonable attorney's fees.
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
        <span class="paragraph-number">23.</span> At all relevant times, Claimant was a "debtor" (Cal. Civ. Code § 1788.2(h)), the obligation was a "consumer debt" (§ 1788.2(f)), and Respondents were "debt collectors" (§ 1788.2(c)) collecting a consumer debt, making their conduct subject to the RFDCPA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">24.</span> Respondents violated multiple provisions of the RFDCPA, including but not limited to:
    </div>

    <div class="bullet-point">
        <strong>California Civil Code § 1788.14(c):</strong> Respondents initiated communication with the Claimant by mail after the Claimant provided written instructions to use a different method of communication (email).
    </div>

    <div class="bullet-point">
        <strong>California Civil Code § 1788.17:</strong> Respondents failed to comply with the provisions of the federal FDCPA (specifically 15 U.S.C. §§ 1692c, 1692d, 1692e, and 1692f), which constitutes a direct violation of the RFDCPA.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">25.</span> Respondents' disregard for Claimant's clear, written instructions and for the plain language of the statutes constituted a knowing and willful violation of California law.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">26.</span> As a direct result of these violations, Claimant suffered actual damages.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">27.</span> Pursuant to California Civil Code § 1788.30, Respondents are liable to Claimant for her actual damages, a statutory penalty of $1,000, and the costs of this action, including reasonable attorney's fees.
    </div>

    <div class="count-header"><strong>COUNT IV: Violations of the California Consumer Credit Reporting Agencies Act (CCRAA)</strong></div>

    <div class="paragraph">
        <span class="paragraph-number">28.</span> Claimant adopts and realleges the foregoing as fully stated herein.
    </div>

    <div class="paragraph">
        <span class="paragraph-number">29.</span> At all relevant times, Claimant was a "consumer" (Cal. Civ. Code § 1785.3(b)), the reports at issue were "consumer credit reports" (§ 1785.3(c)), and Respondents were "users of a consumer credit report" (§ 1785.3(l)), subjecting their conduct to the requirements of the CCRAA.
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
        <span class="paragraph-number">33.</span> Respondents' willful violations of the CCRAA render them liable to Claimant for her actual damages and justify the imposition of punitive damages of $5,000 for each of the six willful violations in order to punish their conduct and deter future misconduct, in addition to the costs of this action and reasonable attorney's fees, pursuant to California Civil Code § 1785.31.
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

    <div class="prayer-section">
        <div class="section-header">PRAYER FOR RELIEF</div>
        
        <div class="paragraph">
            Claimant, Erika Gomez, prays that the Arbitrator enter an award in her favor and against Respondents, granting the following relief:
        </div>

        <div class="paragraph">
            a. <strong>Actual and Compensatory Damages</strong> in an amount to be determined at arbitration for Claimant's emotional distress, financial expenses, and loss of productive time;
        </div>

        <div class="paragraph">
            b. <strong>Statutory Damages</strong> under federal law, including: i. $1,000 for violations of the FDCPA, pursuant to 15 U.S.C. § 1692k; and ii. $1,000 for each of the six willful violations of the FCRA, pursuant to 15 U.S.C. § 1681n.
        </div>

        <div class="paragraph">
            c. <strong>A Statutory Penalty</strong> of $1,000 for violations of California's RFDCPA, pursuant to Cal. Civ. Code § 1788.30;
        </div>

        <div class="paragraph">
            d. <strong>Punitive Damages for Willful Violations of the CCRAA</strong>, specifically $5,000 for each of the six instances where Respondents willfully obtained Claimant's credit report without a permissible purpose, in order to punish their unlawful conduct and to deter them from engaging in such misconduct in the future, pursuant to Cal. Civ. Code § 1785.31;
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
</body>
</html>
"""

def generate_section(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "system", "content": "You are a legal assistant for arbitration complaint drafting."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        # max_tokens=1500
    )
    return response.choices[0].message.content
  
def generate_html(text):
  prompt = f"""
  put the following text :
    "{text}"

  into a HTML template with the following structure:
    "{html_template}"
  
  only give me the HTML content without any additional text or explanation.
  """

  pdf_file_path = f"pdf_files/output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
  html_content = generate_section(prompt)
  html_content = html_template.replace("```html","").replace("```","")
  html_content = html_content.replace("\u2013", "-")
  html_content = html_content.replace("§", "\u00A7")

#   pdfkit.from_string(html_content, pdf_file_path, configuration=config)
  HTML(string=html_content).write_pdf(pdf_file_path)

  print(f"PDF generated successfully as '{pdf_file_path}'")

  return pdf_file_path

if __name__ == "__main__":
    example_text =[
    "```\nAMERICAN ARBITRATION ASSOCIATION\n\n[Case Number]\n\nARBITRATION COMPLAINT\n\nTo Be Submitted To: American Arbitration Association (AAA)\n```",
    "**Party Designation**\n\n**Claimant:**\n\nThe Claimant in this arbitration is Sharese Jackson, a natural person residing in the Commonwealth of Pennsylvania. Ms. Jackson is a \"consumer\" as defined by the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692a(3), as she is alleged to owe a personal, family, or household debt. Additionally, Ms. Jackson is entitled to protection under the Florida Consumer Collection Practices Act (FCCPA) and the Fair Credit Reporting Act (FCRA), which safeguard consumers against unfair and deceptive practices in debt collection and credit reporting.\n\n**Respondents:**\n\n1. **LVNV Funding LLC**  \n   LVNV Funding LLC is a Delaware limited liability company whose primary business involves the purchase and collection of charged-off consumer debts. LVNV operates as a debt buyer and collector, acquiring defaulted debts and seeking to collect them directly or through third-party servicers. LVNV is a \"debt collector\" within the meaning of the FDCPA, 15 U.S.C. § 1692a(6), and is subject to the provisions of the FCCPA and FCRA as it engages in activities affecting consumers' rights and financial interests.\n\n2. **Resurgent Capital Services LP**  \n   Resurgent Capital Services LP is a Delaware limited partnership acting as the debt servicer and collection agent for portfolios owned by LVNV and affiliated entities. Resurgent manages the collection process, oversees third-party collection agencies, and interfaces directly with consumers in connection with the recovery of consumer debts. As such, Resurgent is a \"debt collector\" under the FDCPA, 15 U.S.C. § 1692a(6), and is subject to the FCCPA and FCRA for its consumer debt collection activities.\n\nBoth Respondents engage in consumer debt collection activities that are subject to the FDCPA, FCCPA, and FCRA, impacting the rights and financial interests of consumers, including those residing in Florida.",
    "**Factual Summary**\n\n1. **March 4, 2025**: Claimant Sharese Jackson mailed a convenience letter via USPS Priority Mail to Respondent Resurgent Capital Services LP. The letter specified her preferred communication practices and requested that all future communications be conducted in accordance with these preferences. This action was intended to prevent further inconvenience and emotional distress caused by unsolicited communications.\n\n2. **March 7, 2025**: The convenience letter was delivered to Resurgent Capital Services LP. This delivery established the receipt of Claimant's communication preferences, making any subsequent non-compliant contact a potential violation of the Fair Debt Collection Practices Act (FDCPA), specifically 15 U.S.C. § 1692c(a)(1), which prohibits contacting a consumer at a time or place known to be inconvenient.\n\n3. **March 11, 2025**: Despite the receipt of the convenience letter, Resurgent Capital Services LP sent a letter to Claimant Sharese Jackson. This communication was in direct violation of the FDCPA, 15 U.S.C. § 1692c(a)(1), as it disregarded the specified communication preferences outlined by the Claimant. The receipt of this letter caused Claimant emotional distress and anxiety, as it demonstrated a disregard for her expressed wishes and legal rights under the FDCPA.\n\n4. **Ongoing**: The actions of Resurgent Capital Services LP, in conjunction with LVNV Funding LLC, have resulted in continued emotional distress for Claimant Sharese Jackson. The failure to adhere to the communication preferences has exacerbated her anxiety and has potentially harmed her reputation by suggesting non-compliance with debt obligations. These actions are indicative of unfair and deceptive practices prohibited under the FDCPA and applicable Florida statutes concerning consumer protection and privacy.\n\nEach of these events contributes to the Claimant's assertion that the Respondents have engaged in practices that violate federal consumer protection laws, specifically the FDCPA, and have caused significant emotional harm.",
    "**Introduction and Nature of the Claim**\n\nThis arbitration complaint arises from alleged violations of federal and state consumer protection statutes by Respondents LVNV Funding LLC and Resurgent Capital Services LP in their attempts to collect a consumer debt from Claimant Sharese Jackson. The dispute centers on the Respondents' debt collection practices, which are claimed to have contravened the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692 et seq., the Florida Consumer Collection Practices Act (FCCPA), and the Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681 et seq., as well as applicable Florida privacy statutes.\n\nThe Claimant, Sharese Jackson, a resident of Pennsylvania, alleges that the Respondents engaged in unlawful debt collection activities, including contacting her in a manner known to be inconvenient, in violation of 15 U.S.C. § 1692c(a)(1). Despite receiving a written notice specifying preferred communication practices, the Respondents continued their collection efforts, thereby infringing upon her rights under the FDCPA.\n\nThe statutory basis for this arbitration is grounded in the arbitration clause contained within the original credit agreement with Celtic Bank, which mandates that disputes arising from the agreement be resolved through arbitration under the rules of the American Arbitration Association (AAA). The Claimant seeks resolution of this matter via AAA arbitration, asserting claims under the FDCPA, FCCPA, FCRA, and relevant Florida privacy laws.\n\nThis complaint seeks to hold the Respondents accountable for their alleged statutory violations and to secure appropriate remedies for the Claimant, including but not limited to statutory damages, actual damages, and any other relief deemed just and proper by the arbitration panel. The Claimant respectfully requests that the AAA arbitrate this dispute in accordance with its established procedures and applicable legal standards.",
    "**Jurisdiction and Arbitrability**\n\nThis arbitration proceeding is properly before the American Arbitration Association (\"AAA\") pursuant to the arbitration clause contained within the original credit agreement between the Claimant, Sharese Jackson, and the original creditor, Celtic Bank. The agreement explicitly mandates that any disputes arising from or related to the account, including those involving debt collection practices, shall be resolved through binding arbitration administered by the AAA under its Consumer Arbitration Rules.\n\nThe AAA possesses procedural authority to adjudicate this matter, as the arbitration clause designates the AAA as the forum for dispute resolution. The clause further specifies that the arbitration shall be conducted in accordance with the AAA's rules, which are incorporated by reference into the agreement. This establishes the AAA's jurisdiction over the parties and the subject matter of the dispute.\n\nUnder Florida law, arbitration agreements are enforceable pursuant to the Florida Arbitration Code, Fla. Stat. §§ 682.01 et seq., which upholds the validity and enforceability of arbitration clauses in contracts involving interstate commerce. The Federal Arbitration Act (\"FAA\"), 9 U.S.C. §§ 1-16, further supports the enforceability of such agreements, as the transaction involves interstate commerce given the multi-state operations of the Respondents, LVNV Funding LLC and Resurgent Capital Services LP, and the cross-border nature of the debt collection activities.\n\nThe dispute at hand involves issues arising under the Fair Debt Collection Practices Act (\"FDCPA\"), 15 U.S.C. § 1692 et seq., and the Fair Credit Reporting Act (\"FCRA\"), 15 U.S.C. § 1681 et seq., both of which pertain to federal statutes governing interstate commerce. The Respondents' actions, including the alleged improper communication practices and debt collection efforts directed at the Claimant, a Pennsylvania resident, further substantiate the interstate commerce element requisite for FAA applicability.\n\nAccordingly, the arbitration clause, supported by both federal and Florida state law, confers jurisdiction upon the AAA to resolve the claims presented in this arbitration demand. The Claimant respectfully submits that the AAA is the appropriate forum to adjudicate the alleged violations of the FDCPA and FCRA, as well as any related claims arising from the Respondents' conduct.",
    "**Allegations as to Parties**\n\n1. **Claimant: Sharese Jackson**\n\n   Claimant, Sharese Jackson, is a natural person residing in the Commonwealth of Pennsylvania. For the purposes of this arbitration, Ms. Jackson is considered a \"consumer\" under the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692a(3), as she is alleged to owe a personal, family, or household debt. Under the FDCPA, a \"consumer\" is defined as any natural person obligated or allegedly obligated to pay any debt. Ms. Jackson's status as a consumer entitles her to the protections afforded by the FDCPA against unfair and deceptive debt collection practices.\n\n2. **Respondent: LVNV Funding LLC**\n\n   Respondent LVNV Funding LLC is a Delaware limited liability company whose primary business involves the purchase and collection of charged-off consumer debts. LVNV operates as a debt buyer, acquiring defaulted debts and seeking to collect them either directly or through third-party servicers. LVNV does not originate credit but functions solely as a debt collector. Under the FDCPA, 15 U.S.C. § 1692a(6), LVNV qualifies as a \"debt collector,\" as it regularly collects or attempts to collect debts owed or due, or asserted to be owed or due, to another. LVNV's activities fall within the scope of the FDCPA, which aims to eliminate abusive debt collection practices and protect consumers like Ms. Jackson.\n\n3. **Respondent: Resurgent Capital Services LP**\n\n   Respondent Resurgent Capital Services LP is a Delaware limited partnership acting as the debt servicer and collection agent for portfolios owned by LVNV and affiliated entities. Resurgent manages the collection process, oversees third-party collection agencies, and interfaces directly with consumers to recover consumer debts. As such, Resurgent is also a \"debt collector\" under the FDCPA, 15 U.S.C. § 1692a(6), as it regularly collects or attempts to collect debts using the mail, telephone, and electronic communications. Resurgent's actions are subject to the FDCPA's provisions, which regulate the conduct of debt collectors to prevent harassment and abuse of consumers.\n\nBoth LVNV and Resurgent, through their debt collection activities, engage in practices that affect the rights, financial interests, and well-being of consumers, including Ms. Jackson. Their roles as debt collectors under the FDCPA subject them to the statutory requirements and prohibitions designed to protect consumers from unfair, deceptive, and abusive debt collection practices.",
    "**Factual Allegations**\n\nClaimant Sharese Jackson, a consumer residing in Pennsylvania, brings forth this arbitration complaint against Respondents LVNV Funding LLC and Resurgent Capital Services LP, alleging violations of the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692 et seq., and the Florida Consumer Collection Practices Act (FCCPA), Fla. Stat. § 559.55 et seq. The Respondents, acting as debt collectors, engaged in conduct that contravened the protections afforded to consumers under these statutes.\n\nOn March 4, 2025, Ms. Jackson, exercising her rights under the FDCPA, sent a convenience letter via USPS Priority Mail to Resurgent, specifying her preferred communication practices. This letter was duly delivered on March 7, 2025. Despite receiving this explicit notification, Resurgent dispatched a letter dated March 11, 2025, to Ms. Jackson. This communication was made in direct violation of 15 U.S.C. § 1692c(a)(1), which prohibits debt collectors from contacting consumers at times or places known to be inconvenient to the consumer, after receiving such written notice.\n\nThe actions of Resurgent, under the management and direction of LVNV, demonstrate a disregard for the statutory requirements designed to protect consumers from harassment and abuse in debt collection practices. By failing to adhere to the specified communication preferences of Ms. Jackson, Resurgent engaged in conduct that is both unfair and deceptive, violating the FDCPA's mandate to respect consumer privacy and communication preferences.\n\nFurthermore, the conduct of Resurgent and LVNV also constitutes a breach of the FCCPA, which parallels the FDCPA in prohibiting abusive and harassing debt collection practices. The FCCPA, under Fla. Stat. § 559.72, explicitly prohibits communication with a debtor when such communication is known to be inconvenient to the debtor. The Respondents' actions, therefore, not only violated federal law but also contravened Florida's consumer protection statutes, which are applicable due to the nature of the Respondents' business operations affecting consumers nationwide, including those in Florida.\n\nThe sequence of events illustrates a pattern of misconduct by the Respondents, characterized by their failure to respect the legal rights of the consumer. This pattern of behavior underscores a systemic issue within the Respondents' debt collection practices, which prioritize aggressive collection tactics over compliance with statutory obligations. Such conduct has caused undue stress and inconvenience to Ms. Jackson, warranting the intervention of this arbitration forum to address and rectify the violations committed by the Respondents.",
    "**Practices of the Respondent**\n\nThe Respondents, LVNV Funding LLC and Resurgent Capital Services LP, have engaged in systemic and repeated misconduct in their debt collection practices, violating multiple provisions of the Fair Debt Collection Practices Act (FDCPA), the Florida Consumer Collection Practices Act (FCCPA), and the Fair Credit Reporting Act (FCRA). These violations have caused significant harm to the Claimant, Sharese Jackson, including emotional distress, reputational damage, and invasion of privacy.\n\n1. **Violations of the FDCPA:**\n   - **15 U.S.C. § 1692c(c):** The Respondents continued to communicate with the Claimant after receiving a written notice to cease communication. Despite the Claimant's clear directive, the Respondents persisted in their collection efforts, disregarding the Claimant's rights under the FDCPA.\n   - **15 U.S.C. § 1692d:** The Respondents engaged in conduct the natural consequence of which was to harass, oppress, or abuse the Claimant. This includes repeated communications after being informed of the Claimant's preferred communication practices, causing undue stress and anxiety.\n   - **15 U.S.C. § 1692e(8):** The Respondents failed to communicate accurately regarding the disputed nature of the debt, thereby misrepresenting the status of the debt to third parties, including credit reporting agencies.\n   - **15 U.S.C. § 1692f:** The Respondents employed unfair and unconscionable means to collect the alleged debt, including unauthorized charges and fees not permitted by the original agreement.\n\n2. **Violations of the FCCPA:**\n   - **Fla. Stat. § 559.72(7):** The Respondents willfully engaged in conduct that could reasonably be expected to abuse or harass the Claimant, including persistent communication despite knowing the Claimant's communication preferences.\n   - **Fla. Stat. § 559.72(8):** The Respondents falsely represented the character, amount, or legal status of the debt, misleading the Claimant and third parties about the legitimacy of the debt.\n   - **Fla. Stat. § 559.72(9):** The Respondents attempted to enforce a debt that they knew was not legitimate or was disputed, further exacerbating the Claimant's distress and confusion.\n\n3. **Violations of the FCRA:**\n   - **15 U.S.C. § 1681b(f):** The Respondents accessed the Claimant's credit report without a permissible purpose, violating the Claimant's privacy rights.\n   - **15 U.S.C. § 1681s-2(a)(1):** The Respondents furnished information to credit reporting agencies that they knew or had reasonable cause to believe was inaccurate, damaging the Claimant's creditworthiness and reputation.\n   - **15 U.S.C. § 1681s-2(a)(3):** The Respondents failed to notify credit reporting agencies of the disputed nature of the debt, further perpetuating inaccuracies in the Claimant's credit report.\n\nThe Respondents' actions have caused significant emotional distress to the Claimant, who has suffered anxiety and stress due to the persistent and unlawful collection practices. Additionally, the Respondents' misrepresentations and unauthorized access to the Claimant's credit information have resulted in reputational damage and an invasion of privacy, further compounding the harm experienced by the Claimant. These practices demonstrate a pattern of systemic misconduct that violates the Claimant's rights under federal and Florida law.",
    "**CAUSES OF ACTION**\n\n**COUNT I – Violation of the Fair Debt Collection Practices Act (FDCPA)**\n\n1. **Incorporation of Prior Allegations**\n   - Claimant Sharese Jackson hereby incorporates by reference all preceding paragraphs as though fully set forth herein.\n\n2. **Legal Basis**\n   - This count is brought under the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692 et seq., which prohibits debt collectors from engaging in abusive, deceptive, and unfair practices.\n\n3. **Application of Facts to Legal Elements**\n   - **Debt Collector Status**: Respondents LVNV Funding LLC and Resurgent Capital Services LP are \"debt collectors\" as defined by 15 U.S.C. § 1692a(6) because they regularly collect or attempt to collect debts owed or due another.\n   - **Prohibited Communication**: On March 11, 2025, Resurgent sent a letter to Claimant after receiving a convenience letter specifying preferred communication practices. This constitutes a violation of 15 U.S.C. § 1692c(a)(1), which prohibits communication at a time or place known to be inconvenient to the consumer.\n   - **Misrepresentation**: The communication from Resurgent falsely represented the character, amount, or legal status of the debt, in violation of 15 U.S.C. § 1692e(2)(A).\n\n4. **Damages Suffered**\n   - As a direct and proximate result of Respondents' violations of the FDCPA, Claimant has suffered emotional distress, anxiety, and inconvenience. Claimant has also incurred costs associated with addressing these unlawful communications.\n\n5. **Demand for Relief**\n   - Claimant respectfully requests that the arbitrator award the following relief:\n     - Statutory damages pursuant to 15 U.S.C. § 1692k(a)(2)(A).\n     - Actual damages for emotional distress and inconvenience.\n     - Costs and reasonable attorney's fees pursuant to 15 U.S.C. § 1692k(a)(3).\n     - Any other relief deemed just and proper by the arbitrator.\n\n**COUNT II – Violation of the Florida Consumer Collection Practices Act (FCCPA)**\n\n1. **Incorporation of Prior Allegations**\n   - Claimant Sharese Jackson hereby incorporates by reference all preceding paragraphs as though fully set forth herein.\n\n2. **Legal Basis**\n   - This count is brought under the Florida Consumer Collection Practices Act (FCCPA), Fla. Stat. § 559.55 et seq., which prohibits certain debt collection practices.\n\n3. **Application of Facts to Legal Elements**\n   - **Debt Collector Status**: Respondents are \"debt collectors\" as defined by Fla. Stat. § 559.55(7) because they engage in the collection of consumer debts.\n   - **Prohibited Conduct**: Respondents engaged in conduct that was intended to harass and oppress Claimant by continuing to communicate in a manner known to be inconvenient, in violation of Fla. Stat. § 559.72(7).\n\n4. **Damages Suffered**\n   - As a result of Respondents' violations of the FCCPA, Claimant has suffered emotional distress and inconvenience. Claimant has also incurred costs related to addressing these unlawful communications.\n\n5. **Demand for Relief**\n   - Claimant respectfully requests that the arbitrator award the following relief:\n     - Statutory damages pursuant to Fla. Stat. § 559.77(2).\n     - Actual damages for emotional distress and inconvenience.\n     - Costs and reasonable attorney's fees pursuant to Fla. Stat. § 559.77(2).\n     - Any other relief deemed just and proper by the arbitrator.\n\n**COUNT III – Violation of the Fair Credit Reporting Act (FCRA)**\n\n1. **Incorporation of Prior Allegations**\n   - Claimant Sharese Jackson hereby incorporates by reference all preceding paragraphs as though fully set forth herein.\n\n2. **Legal Basis**\n   - This count is brought under the Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681 et seq., which regulates the collection, dissemination, and use of consumer information, including consumer credit information.\n\n3. **Application of Facts to Legal Elements**\n   - **Furnisher of Information**: Respondents, as furnishers of information to consumer reporting agencies, are subject to the requirements of the FCRA.\n   - **Failure to Correct Information**: Respondents failed to conduct a reasonable investigation into the disputed debt and continued to report inaccurate information to credit reporting agencies, in violation of 15 U.S.C. § 1681s-2(b).\n\n4. **Damages Suffered**\n   - As a result of Respondents' violations of the FCRA, Claimant has suffered damage to her credit reputation, emotional distress, and financial harm.\n\n5. **Demand for Relief**\n   - Claimant respectfully requests that the arbitrator award the following relief:\n     - Statutory damages pursuant to 15 U.S.C. § 1681n(a)(1)(A).\n     - Actual damages for credit damage, emotional distress, and financial harm.\n     - Punitive damages pursuant to 15 U.S.C. § 1681n(a)(2).\n     - Costs and reasonable attorney's fees pursuant to 15 U.S.C. § 1681n(a)(3).\n     - Any other relief deemed just and proper by the arbitrator.",
    "**Prayer for Relief**\n\nWHEREFORE, Claimant Sharese Jackson respectfully requests that the Arbitrator grant the following relief against Respondents LVNV Funding LLC and Resurgent Capital Services LP:\n\n1. **Actual Damages**: \n   - Award Claimant actual damages for emotional distress, financial loss, and reputational harm suffered as a result of Respondents' unlawful debt collection practices, in an amount to be determined at arbitration.\n\n2. **Statutory Damages**:\n   - Award Claimant statutory damages pursuant to the Fair Debt Collection Practices Act (FDCPA), 15 U.S.C. § 1692k(a)(2)(A), in the maximum amount allowed by law for Respondents' violations of the FDCPA.\n   - Award Claimant statutory damages pursuant to the Florida Consumer Collection Practices Act (FCCPA), Fla. Stat. § 559.77(2), in the maximum amount allowed by law for Respondents' violations of the FCCPA.\n   - Award Claimant statutory damages pursuant to the Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681n(a)(1)(A) and § 1681o(a)(1), in the maximum amount allowed by law for Respondents' violations of the FCRA.\n\n3. **Punitive Damages**:\n   - Award Claimant punitive damages as permitted under the FCCPA, Fla. Stat. § 559.77(2), and the FCRA, 15 U.S.C. § 1681n(a)(2), to deter Respondents and others from engaging in similar unlawful conduct in the future.\n\n4. **Costs and Attorney Fees**:\n   - Award Claimant the costs of arbitration, including all filing fees and expenses incurred.\n   - Award Claimant reasonable attorney fees pursuant to 15 U.S.C. § 1692k(a)(3), Fla. Stat. § 559.77(2), and 15 U.S.C. § 1681n(a)(3) and § 1681o(a)(2), as applicable, for the prosecution of this arbitration.\n\n5. **Injunctive and Equitable Relief**:\n   - Issue an injunction prohibiting Respondents from engaging in further unlawful debt collection practices in violation of the FDCPA, FCCPA, and FCRA.\n   - Order Respondents to correct any inaccurate information reported to credit reporting agencies regarding Claimant's alleged debt, and to notify all relevant parties of such corrections.\n\n6. **Additional Relief**:\n   - Grant such other and further relief as the Arbitrator deems just and proper under the circumstances.\n\nClaimant reserves the right to amend this Prayer for Relief as necessary to conform to the evidence presented and the interests of justice.\n\nRespectfully submitted,\n\n[Claimant's Legal Representative's Name]  \n[Law Firm Name]  \n[Address]  \n[City, State, Zip Code]  \n[Phone Number]  \n[Email Address]  \n\nAttorney for Claimant Sharese Jackson",
    "**Signature Block**\n\n[Authorized Representative Name]  \n[Title: Claimant or Legal Representative]  \n[Address: Placeholder for Address]  \n[Email: Placeholder for Email]  \n[Phone: Placeholder for Phone Number]  \n\nPlease ensure that the placeholders are filled with the appropriate information before submission."
  ]
    # output_pdf_path =  generate_html(example_text)
    # print(f"Generated PDF file at: {output_pdf_path}")
    # Step 4: Create PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.add_page()

    for content in example_text:
        pdf.set_font("Arial", 'B', size=14)
        # pdf.multi_cell(0, 10, title)
        pdf.set_font("Arial", size=12)
        content = content.replace("\u2013", "-")  # Replace en-dash with normal dash
        content = content.encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 10, content)
        pdf.ln()

    # Step 5: Save & return PDF
    output_path = "Newoutput.pdf"
    pdf.output(output_path)