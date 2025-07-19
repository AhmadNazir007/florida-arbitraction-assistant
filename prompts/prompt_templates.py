from .section_instructions import section_instructions
from .section_examples import section_examples

def generate_section_prompt(section_name, user_facts, retrieved_context):
    instruction = section_instructions.get(section_name, "Follow AAA arbitration complaint format.")
    example = section_examples.get(section_name, "")

    prompt = f"""
ROLE:
You are a legal assistant specializing in AAA arbitration complaints under FDCPA, FCCPA, FCRA, and state privacy laws.

CONTEXT FROM DATABASE:
{retrieved_context or "[None]"}

FACTS FROM USER:
{user_facts or "[None]"}

TASK:
Draft the section titled: **{section_name}**

INSTRUCTIONS:
{instruction.strip()}

FORMAT & STYLE:
- Narrative paragraph form (not bullets)
- Use statutes like “15 U.S.C. § 1692d” inline
- Write in the tone of legal pleadings

EXAMPLE OUTPUT FOR THIS SECTION:
{example.strip()}
"""
    return prompt
