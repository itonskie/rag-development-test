from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama_service import llm_with_rag_runnable
from init_vectordb import init_vectordb_main
from vector_store import vector_store_manager  # Import vector_store_manager

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query(request: QueryRequest):
    try:
        # Get the LLM pipeline
        rag_chain = llm_with_rag_runnable()
        
        # Extract the question string from the request body
        question = request.question
        
        # Retrieve relevant documents
        retriever = vector_store_manager.get_retriever()
        retrieved_docs = retriever.get_relevant_documents(question)
        retrieved_snippets = [doc.page_content for doc in retrieved_docs]
        
        # Invoke the model with the extracted question string
        response = rag_chain.invoke(question)
        
        # Format the response to match the expected output format
        result = {
            "query": question,
            "retrieved_docs": retrieved_snippets,
            "answer": response.content
        }
        
        # Return the result
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    init_vectordb_main()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
