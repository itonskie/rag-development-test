from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from vector_store import vector_store_manager
from config import OLLAMA_BASE_URL, OLLAMA_MODEL_NAME

def llm_with_rag_runnable():
    # Initialize vector store
    vector_store_manager.initialize()
    retriever = vector_store_manager.get_retriever()

    chatllama = ChatOllama(
        base_url=OLLAMA_BASE_URL,
        model=OLLAMA_MODEL_NAME,
    )

    rag_prompt = ChatPromptTemplate([
        ("human", """
        You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. 
        If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
        Question: {question}
        Context: {context}
        Answer:
        """)
    ])

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | rag_prompt
        | chatllama
    )

    return rag_chain
