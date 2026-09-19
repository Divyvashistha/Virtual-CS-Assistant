# Virtual CS Assistant

An AI-powered research assistant designed to help with Company Secretarial, corporate law, and regulatory research.

The project combines a Large Language Model (LLM) with Retrieval-Augmented Generation (RAG) to retrieve relevant information from a user-provided knowledge base and use that context to generate responses.

## Features

- AI-powered question answering
- Retrieval-Augmented Generation (RAG)
- Document-based knowledge retrieval
- Custom prompts for legal and compliance-oriented queries
- Streamlit-based user interface
- Modular RAG and LLM processing pipeline
- Extensible knowledge base for additional regulatory material

## How It Works

The assistant follows a retrieval-augmented workflow:

```text
User Query
    │
    ▼
Streamlit Interface
    │
    ▼
Query Processing
    │
    ▼
Knowledge Base Retrieval
    │
    ▼
Relevant Context
    │
    ▼
LLM + Custom Prompt
    │
    ▼
Generated Response
