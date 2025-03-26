# config.py

CONNECTION_STRING = "postgresql+psycopg://postgres:postgres@db:5432/postgres"
COLLECTION_NAME = "my_docs"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Ollama settings
OLLAMA_BASE_URL = "http://ollama:11434"
OLLAMA_MODEL_NAME = "llama3.2"

# Retriever settings
RETRIEVER_K = 2  # Return only 2 documents
