from langchain_core.documents import Document
from langchain_postgres import PGVector
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from typing import List
from config import CONNECTION_STRING, COLLECTION_NAME, EMBEDDING_MODEL

DATA = [
    "Cybersecurity is the practice of protecting systems and networks from attacks. It includes measures like firewalls, intrusion detection, and encryption.",
    "A zero-day vulnerability is an undisclosed flaw in software that attackers can exploit before the vendor issues a fix.",
    "Two-factor authentication (2FA) enhances security by requiring users to provide two forms of verification before gaining access.",
    "Machine learning models require large datasets and are often fine-tuned to improve accuracy for specific tasks.",
    "The CIA triad—Confidentiality, Integrity, and Availability—is a foundational concept in cybersecurity."
]

def create_documents(data: List[str]) -> List[Document]:
    """Convert raw text data into Document objects."""
    print("Creating documents from raw data...")
    documents = [Document(page_content=item) for item in data]
    print("Document creation completed.")
    return documents

def check_existing_docs(vector_store: PGVector, texts: list[str]) -> set[str]:
    """Check if documents with the same text already exist in the database."""
    existing_texts = set()
    
    try:
        # Use the vector_store's `query` method to check for existing texts
        for text in texts:
            results = vector_store.similarity_search(text, k=1)
            if results:
                for result in results:
                    existing_texts.add(result.metadata.get("page_content"))
    except Exception as e:
        print(f"Error checking for existing documents: {e}")
    
    return existing_texts

def initialize_vector_database(docs: List[Document]) -> None:
    try:
        print("Initializing Vector Database...")
        print("Loading Embeddings Model Configuration...")
        
        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        print("Embeddings Model Configuration Loaded.")
        
        print("Initializing PGVector store...")
        vector_store = PGVector(
            embeddings=embeddings,
            collection_name=COLLECTION_NAME,
            connection=CONNECTION_STRING,
            use_jsonb=True,
        )
        print("PGVector store initialized.")
        
        # Prepare document texts for the check
        doc_texts = [doc.page_content for doc in docs]

        # Check which documents already exist in the database
        print("Checking for existing documents in the database...")
        existing_texts = check_existing_docs(vector_store, doc_texts)

        # Filter out documents that already exist
        new_docs = []
        for doc in docs:
            if doc.page_content not in existing_texts:
                doc.metadata = {"page_content": doc.page_content}  # Store text in metadata
                new_docs.append(doc)
            else:
                print(f"Skipping duplicate document: {doc.page_content[:30]}...")

        # Add only new documents to the vector store
        if new_docs:
            print(f"Adding {len(new_docs)} new documents to the vector store...")
            vector_store.add_documents(new_docs)
            print("Documents successfully added to the vector store.")
        else:
            print("No new documents to add.")

    except OperationalError as e:
        raise ConnectionError(f"Failed to connect to the database: {e}")
    except SQLAlchemyError as e:
        raise Exception(f"Database error: {e}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def init_vectordb_main():
    """Main function to create and initialize the vector database."""
    documents = create_documents(DATA)
    initialize_vector_database(documents)
