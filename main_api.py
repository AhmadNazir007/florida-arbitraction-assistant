from fastapi import FastAPI, Body
from rag.rag_retrieval import retrieve_context
from prompts.prompt_templates import generate_section_prompt, section_instructions
from rag.generate_section import generate_section
from rag.dynamic_query import generate_dynamic_query
from template import generate_section_html, generate_pdf_file
from template import section_html_templates
from pydantic import BaseModel


app = FastAPI(title="Florida Arbitration Complaint Assistant")

document_list = [
    "pdf_files/FDCPA Quick Reference Guide.pdf",
    "pdf_files/Florida FCCPA Statues.pdf",
    "pdf_files/Lawyers CheatSheet - FDCPA - Violations Checklist and Cheat Sheet.doc.pdf",
    "pdf_files/Fair Credit Reporting Act.pdf",
    "pdf_files/debt collector failed to established assignment of contract.pdf",
    "pdf_files/Contacting third party in connection of debt .pdf",
]

def generate_arbitration_section(section_name: str, user_facts: str, previous_sections: str = Body(...)):
    prompt = generate_section_prompt(section_name, user_facts, "")
    query = generate_dynamic_query(section_name, prompt, user_facts, [])
    context = retrieve_context(query)
    prompt = generate_section_prompt(section_name, user_facts, context)
    output = generate_section(prompt)
    html_response = generate_section_html(section_name, output, previous_sections)
    return output, html_response

class UserFactsInput(BaseModel):
    user_facts: str

@app.post("/generate-rag-case/")
def generate_rag_case(data: UserFactsInput):
    user_facts = data.user_facts  
    section_generated = []
    html_sections = []

    print("------------- User facts Received -----------")
    print(f"\n\n {user_facts} \n\n")
    print("-----------------------------------------\n\n")

    for section_name, _ in section_instructions.items():
        previous_sections = "\n".join(html_sections) if html_sections else "This is the First Section."
        html_response = generate_section_html(section_name, section_html_templates.get(section_name, ""), previous_sections)
        section_generated.append(html_response)
        html_sections.append(html_response)

    print("------------- All Sections Generated -----------")
    
    pdf_path = generate_pdf_file(html_sections)

    return {
        "Final": section_generated,
        "pdf_path": pdf_path,
        "message": "All sections generated successfully and PDF created."
    }