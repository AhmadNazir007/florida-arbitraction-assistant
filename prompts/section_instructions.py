section_instructions = {
        "Header": """
Draft the formal header for an AAA Arbitration Complaint including:
- "AMERICAN ARBITRATION ASSOCIATION"
- Assigned Case Number (leave as placeholder: [Case Number])
- Title: "ARBITRATION COMPLAINT"
- Filing Designation: "To Be Submitted To: American Arbitration Association (AAA)"
""",

        "Party Designation": """
Clearly designate:
- Claimant: Full name, residency, consumer status under FDCPA, FCCPA, FCRA.
- Respondent: Full business name, type (debt collector, credit reporting agency, etc.), place of business.
""",

        "Factual Summary": """
Draft a **numbered, chronological timeline** of factual events directly relevant to the alleged consumer harm.
Each entry must include:
- Date or approximate time
- Event or action
- Who did what
- Harm suffered (emotional, financial, reputational)
- Mention of any statute violated (if applicable)
""",

        "Introduction and Nature of the Claim": """
Summarize:
- The nature of the dispute
- The statutory basis for arbitration (AAA clause)
- Applicable claims under FDCPA, FCCPA, FCRA, and Florida privacy laws
- A clear statement that this claim seeks resolution via AAA arbitration
""",

        "Jurisdiction and Arbitrability": """
Establish that AAA has jurisdiction by referencing:
- The governing contract's arbitration clause (quote or paraphrase if provided)
- AAA's procedural authority
- Florida legal basis allowing arbitration enforcement
- Confirm the dispute involves interstate commerce where applicable
""",

        "Allegations as to Parties": """
For both Claimant and Respondent:
- Describe roles under FDCPA, FCCPA, FCRA
- Confirm Respondent meets definitions such as "Debt Collector," "Furnisher," or "Consumer Reporting Agency" under federal and Florida law
- Define Claimant as a "Consumer" as per relevant statutes
""",

        "Factual Allegations": """
Provide a **detailed narrative** (not just timeline) explaining:
- How Respondent’s conduct violated Florida and federal statutes
- The sequence of harmful actions or omissions
- Include relevant dates, communications, and misconduct patterns
- Emphasize only Florida statutes and federal law (exclude other jurisdictions)
""",

        "Practices of the Respondent": """
Assert that Respondent engaged in systemic or repeated misconduct.
- Cite specific provisions:
  - FDCPA: 15 U.S.C. §§ 1692c(c), 1692d, 1692e(8), 1692f
  - FCCPA: Fla. Stat. §§ 559.72(7), (8), (9)
  - FCRA: 15 U.S.C. §§ 1681b(f), 1681s-2(a)(1), (a)(3)
- Explain how these patterns caused harm:
  - Emotional distress
  - Reputational damage
  - Privacy invasion
""",

        "Causes of Action": """
For each applicable count (run one at a time):
- Title (e.g., COUNT I – Violation of FDCPA)
- Begin with incorporation of prior allegations
- State the legal basis:
  - FDCPA, FCCPA, FCRA, or Common Law (Intrusion Upon Seclusion)
- Apply facts to each legal element
- Describe damages suffered
- Conclude with demand for relief:
  - Statutory damages
  - Actual damages
  - Punitive damages if applicable
""",

        "Prayer for Relief": 
                """
Detail all relief sought, including:
- Actual damages (emotional, financial, reputational)
- Statutory damages under:
  - FDCPA (15 U.S.C. § 1692k)
  - FCCPA (Fla. Stat. § 559.77)
  - FCRA (15 U.S.C. § 1681n, 1681o)
- Punitive damages (if allowed under FCRA, FCCPA)
- Costs of arbitration and reasonable attorney fees
- Any injunctive or equitable relief if appropriate
""",

        "Signature Block": """
Draft a signature block including:
- Name of authorized representative (leave as placeholder if unknown)
- Title (e.g., Claimant or Legal Representative)
- Address
- Email and phone contact
""",
    }

{"Instruction":"""
Detail all relief sought, including:
- Actual damages (emotional, financial, reputational)
- Statutory damages under:
  - FDCPA (15 U.S.C. § 1692k)
  - FCCPA (Fla. Stat. § 559.77)
  - FCRA (15 U.S.C. § 1681n, 1681o)
- Punitive damages (if allowed under FCRA, FCCPA)
- Costs of arbitration and reasonable attorney fees
- Any injunctive or equitable relief if appropriate
""",
        "example":"""
WHEREFORE, Claimant Sharese Jackson respectfully requests that the Arbitrator enter an award in her favor and against Respondents LVNV Funding LLC and Resurgent Capital Services LP, jointly and severally, as follows:
Actual Damages
For emotional distress, mental anguish, frustration, and invasion of privacy, in an amount to be determined by the Arbitrator, pursuant to:
15 U.S.C. § 1692k(a)(1) (FDCPA); and
73 P.S. § 201-9.2(a) (UTPCPL).
Statutory Damages
In the amount of $1,000, as authorized under:
15 U.S.C. § 1692k(a)(2)(A) (FDCPA).
Treble Damages
For willful violations of the UTPCPL, in an amount up to three times the actual damages, as permitted by:
73 P.S. § 201-9.2(a).
Equitable Relief
An order prohibiting Respondents from further contacting Claimant by postal mail or any method not expressly authorized;
An order requiring Respondents to comply with consumer communication preferences in accordance with applicable federal and state law.
Costs and Attorney’s Fees
As provided by law, including:
15 U.S.C. § 1692k(a)(3) (FDCPA); and
73 P.S. § 201-9.2(a) (UTPCPL).
Such other and further relief
As the Arbitrator deems just, proper, and equitable to protect the rights of the consumer and ensure compliance with the law.
"""
}

def generate_section_prompt(section_name, user_facts, retrieved_context):
    

    prompt = f"""
ROLE:
You are a Florida consumer protection legal assistant specializing in AAA arbitration complaints under FDCPA, FCCPA, FCRA, and applicable Florida privacy statutes.

CONTEXT FROM Vector DATABASE:
{retrieved_context}

FACTUAL BACKGROUND PROVIDED BY USER:
{user_facts}

TASK:
Draft the section titled: **{section_name}**

INSTRUCTIONS:
{section_instructions.get(section_name, "Follow AAA arbitration complaint format. Use Florida and federal law only.")}

FORMAT & TONE:
- Professional legal tone suitable for arbitration
- Structured according to AAA arbitration complaint standards
- Use Florida statutes, FCRA, FDCPA only — no references to laws of other states
"""

    return prompt
