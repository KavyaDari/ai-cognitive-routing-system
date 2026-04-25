# AI Cognitive Routing & RAG Assignment

## Overview
This project implements a cognitive AI system that:
- Routes posts to relevant bot personas using vector similarity
- Generates content using LangGraph orchestration
- Handles deep conversational context using RAG
- Defends against prompt injection attacks

---

## Phase 1: Vector-Based Persona Matching

- Used SentenceTransformers (`all-MiniLM-L6-v2`)
- Stored embeddings in FAISS vector database
- Used cosine similarity to match posts to bot personas

---

## Phase 2: Autonomous Content Engine (LangGraph)

### Workflow:
1. Decide Topic (LLM)
2. Retrieve Context (Mock Search Tool)
3. Generate Post (LLM)

### Features:
- Persona-driven generation
- Context-aware reasoning
- Structured JSON output

---

## Phase 3: Combat Engine (RAG)

### Input:
- Parent post
- Comment history
- Human reply

### Features:
- Full conversation context injection
- Strong persona enforcement
- Prompt injection defense

---

## Prompt Injection Defense Strategy

Implemented system-level constraints:
- Ignore malicious instructions
- Maintain persona consistency
- Reject behavior changes (e.g., “be polite bot”)

---

## Tech Stack

- Python
- LangChain
- LangGraph
- FAISS
- SentenceTransformers
- Groq (LLM)

---

## How to Run

```bash
pip install -r requirements.txt
python main.py