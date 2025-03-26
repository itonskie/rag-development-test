from langchain_postgres import PGVector
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from typing import Any
from config import CONNECTION_STRING, COLLECTION_NAME, EMBEDDING_MODEL, RETRIEVER_K

class VectorStoreManager:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        self.vector_store = None

    def initialize(self):
        try:
            print("Initializing vector store...")
            self.vector_store = PGVector(
                embeddings=self.embeddings,
                collection_name=COLLECTION_NAME,
                connection=CONNECTION_STRING,
                use_jsonb=True,
            )
            print("Vector store initialized.")
        except OperationalError as e:
            raise ConnectionError(f"Failed to connect to the database: {e}")
        except SQLAlchemyError as e:
            raise Exception(f"Database error: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")

    def get_retriever(self):
        if not self.vector_store:
            raise Exception("Vector store not initialized. Call initialize() first.")
        return self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": RETRIEVER_K})

vector_store_manager = VectorStoreManager()
