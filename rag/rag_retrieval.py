from dotenv import load_dotenv
import os
import pinecone
from openai import OpenAI, OpenAIError

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENVIRONMENT")
index_name = os.getenv("INDEX_NAME")
namespace = os.getenv("NAMESPACE")

pc = pinecone.Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)

def get_query_embedding(query):
    try:
        response = client.embeddings.create(
            input=[query],
            model="text-embedding-ada-002"
        )
        return response.data[0].embedding
    except OpenAIError as e:
        raise RuntimeError(f"Embedding failed: {str(e)}")

def retrieve_context(query, top_k=5):
    query_embedding = get_query_embedding(query)
    result = index.query(
        vector=query_embedding,
        top_k=top_k,
        namespace=namespace,
        include_metadata=True
    )
    return "\n\n---\n\n".join([match['metadata']['text'] for match in result['matches']])
