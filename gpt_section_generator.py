from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_section(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a legal assistant for arbitration complaint drafting."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        # max_tokens=4000
    )
    return response.choices[0].message.content

def llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content


if __name__ == '__main__':
    # Example usage
    example_prompt = "Write me a essay"
    section_output = generate_section(example_prompt)
    print(section_output)