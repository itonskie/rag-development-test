# Rag Development Test

## Table of Contents
- [Overview](#overview)
- [Components](#components)
- [Why This Stack?](#why-this-stack)
  - [LangChain](#langchain)
  - [Ollama](#ollama)
  - [PGVector](#pgvector)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Enter the Project Directory](#enter-the-project-directory)
  - [Run Docker Compose](#run-docker-compose)
  - [Important Note](#important-note)
  - [Accessing the Application](#accessing-the-application)
  - [Warning](#warning)
  - [Memory Limitation](#memory-limitation)

## Overview
The purpose of this project is to demonstrate the process of building a **RAG (Retrieval-Augmented Generation)** application using **Large Language Models (LLMs)** and a **Vector Database**. The entire setup is packaged within a **Docker Compose file** for simplicity and ease of use.

## Components
This project comprises three main parts:
1. **PGVector (PostgreSQL Database):** A robust and persistent vector database extension for PostgreSQL, offering reliability and disk-based storage.
2. **Ollama Image (LLama 3.2 Model):** A free and easy-to-use LLM implementation pulled from Docker Hub, designed to be OpenAI API-compliant.
3. **FastAPI Wrapper:** A lightweight, efficient web server used to interface with the RAG pipeline.

## Why This Stack?
### LangChain
I selected **LangChain** for orchestrating the RAG process, despite its high-level abstractions which can sometimes be restrictive. The reason for choosing LangChain is its rich ecosystem of community-driven integrations, allowing various components to work seamlessly together within a single framework.

### Ollama
I chose **Ollama** over alternatives like OpenAI and Claude for several reasons:
- **Ease of Use:** It provides a ready-made Docker image on Docker Hub, simplifying setup.
- **Cost Efficiency:** The models are free and easy to pull, without complicated licensing restrictions.
- **Compatibility:** Being **OpenAI API-compliant**, it integrates smoothly with LangChain, making the development process nearly identical to using OpenAI’s API.

### PGVector
I opted for **PGVector** as the vector database for these reasons:
- **Persistence:** Unlike in-memory databases, PGVector persists data to disk, ensuring data safety even during unexpected shutdowns.
- **Familiarity:** PostgreSQL is a widely-adopted and reliable database technology with a strong foundation.
- **Scalability:** Disk-based storage is simpler to manage and scale, making PGVector a practical choice for a solo developer.

## Getting Started
### Clone the Repository
```bash
    git clone https://github.com/itonskie/rag-development-test.git
```

### Enter the Project Directory
```bash
    cd rag-development-test
```

### Run Docker Compose
```bash
    docker compose up
```

### Important Note
The initial run may take some time as it will download the following components:
- The **embedding model**
- The **LLama 3.2 model**
- Other required Docker images

### Accessing the Application
Once the setup is complete, the application will be accessible at:
```
http://localhost:8000/docs
```

### Warning
Ensure that port **8000** is not occupied by any other application. If another application is using this port, the setup will fail.

### Memory Limitation
This is a simple development test, and **no memory functionality** has been implemented. Each request is processed independently, with no long-term memory storage.

