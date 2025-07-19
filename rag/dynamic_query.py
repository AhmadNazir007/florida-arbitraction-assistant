from openai import OpenAI, OpenAIError
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_dynamic_query(section_name: str, section_prompt: str, user_facts: str, document_list: list) -> str:
    document_summary = "\n".join([f"- {doc}" for doc in document_list])

    system_prompt = """
You are an expert legal research assistant specializing in Florida consumer protection law, FDCPA, FCCPA, and FCRA.
Output ONLY the optimized semantic search query string. No extra text.
"""

    user_prompt = f"""
DOCUMENTS:
{document_summary}

SECTION: {section_name}

SECTION PURPOSE:
{section_prompt}

FACTUAL BACKGROUND:
{user_facts}

TASK:
Generate a focused semantic search query string.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        raise RuntimeError(f"Query generation failed: {str(e)}")
