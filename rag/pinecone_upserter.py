import os
import pdfplumber
from uuid import uuid4
from dotenv import load_dotenv
from openai import OpenAI
from pinecone import Pinecone, ServerlessSpec
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENVIRONMENT")
index_name = os.getenv("INDEX_NAME")
namespace = os.getenv("NAMESPACE")

client = OpenAI(api_key=openai_api_key)

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)

# Create index if not exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(index_name)

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def split_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(text)

def get_embedding(text):
    response = client.embeddings.create(
        input=[text],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding
 
def upsert_pdf_to_pinecone(file_path):
    text = extract_text_from_pdf(file_path)
    if not text.strip():
        print(f"⚠️ No text extracted from {file_path}. Skipping.")
        return

    chunks = split_text(text)
    vectors = []

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        vector_id = f"{os.path.basename(file_path)}-{i}-{uuid4()}"
        vectors.append({
            "id": vector_id,
            "values": embedding,
            "metadata": {
                "text": chunk,
                "source": os.path.basename(file_path)
            }
        })

    index.upsert(vectors=vectors, namespace=namespace)
    print(f"✅ Upserted {len(vectors)} vectors from '{os.path.basename(file_path)}'")
    return file_path, [v["id"] for v in vectors]

if __name__ == "__main__":
    folder_path = "pdf_files"
    pinecone_file_ids = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            try:
                result = upsert_pdf_to_pinecone(file_path)
                if result:
                    file_path, vector_ids = result
                    for vector_id in vector_ids:
                        pinecone_file_ids.append(f"{file_path},{vector_id}\n")
            except Exception as e:
                print(f"❌ Failed to upsert '{filename}': {str(e)}")

    with open("Pinecone_ids.txt", "a") as f:
        f.writelines(pinecone_file_ids)

    print("🎉 All PDF files processed and uploaded to Pinecone.")
