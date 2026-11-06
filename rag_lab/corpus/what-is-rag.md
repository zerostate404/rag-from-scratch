---
title: What Is a RAG Pipeline
topic: rag
difficulty: easy
---
# Question
Explain how a RAG pipeline works end to end.

# Key points
- RAG = Retrieval-Augmented Generation: retrieve relevant documents, then generate a grounded answer
- Indexing phase (offline): chunk corpus → embed chunks → store vectors + metadata
- Query phase (online): embed query → retrieve top-k by cosine/similarity → put chunks in prompt → call LLM
- Grounding reduces hallucination but does not eliminate it — the model can still ignore or misread retrieved text
- Chunking strategy and top-k strongly affect quality; there's no single correct setting

# Reference answer
RAG has two phases. Offline (indexing): split the corpus into chunks, embed each chunk with an embedding model, and store the vectors alongside metadata (source, heading, position) in a vector store. Online (query): embed the user's query with the same embedding model, find the top-k nearest chunks by cosine similarity, and inject those chunks into the prompt as context — usually as a numbered or tagged block. The LLM is then asked to answer using the provided context. This grounds the model in real text and reduces hallucination, but it doesn't eliminate it: the model can still misread, ignore, or blend retrieved text with its own training. The two levers that most affect quality are chunking strategy (chunk size, overlap, whether to split on semantic boundaries like headings) and top-k (too few → miss relevant context; too many → dilute the prompt and blow the context window). Retrieval quality is usually the bottleneck, not the LLM.