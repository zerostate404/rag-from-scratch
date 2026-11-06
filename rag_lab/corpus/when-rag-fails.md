---
title: When RAG Fails
topic: rag
difficulty: medium
---
# Question
What are common reasons a RAG system gives wrong or unhelpful answers?

# Key points
- Retrieval miss: the relevant document wasn't retrieved (bad chunking, weak embedding model, top-k too small)
- Retrieval noise: retrieved chunks are irrelevant, and the LLM gets confused or dilutes the signal
- Context ignored: the right chunk was retrieved but the LLM ignored or misread it
- Hallucination: LLM adds claims not in the retrieved context
- Chunking/embedding mismatch: query phrasing and document phrasing live in different semantic regions
- Fixes are ordered: fix retrieval first, then prompt, then chunking — most failures are retrieval

# Reference answer
Most RAG failures are retrieval failures, not generation failures. First, the relevant chunk simply wasn't retrieved — the embedding ranked it below top-k because of chunking (idea split across chunks), a weak embedding model, or a query phrased very differently from the document. The most common root cause is vocabulary mismatch: the user asks "how do I stop my model memorizing" while the note says "overfitting," and embeddings that capture topic rather than synonyms place them just far enough apart to miss. Fixes here are layered: better chunking (split on semantic boundaries, not fixed windows), a stronger embedding model, larger top-k, query rewriting (ask a small LLM to rephrase the query in the corpus's vocabulary), or hybrid search — combine BM25 keyword matching with dense vector retrieval so exact term overlap rescues the cases where embeddings alone drift. Second, the retrieved chunks are noisy: top-k pulled in multiple irrelevant chunks that dilute the signal, and the LLM either ignores them (fine) or gets confused and blends unrelated passages (bad). Fix: tighter top-k, a cross-encoder reranker that scores each retrieved chunk against the query more carefully than cosine can, and a similarity threshold that drops low-scoring chunks before they reach the prompt. Third, the context was retrieved but the model ignored it — it falls back on its training prior and hallucinates. Fix: prompt-level instructions ("answer using only the provided context, and say 'I don't know' otherwise"), structured context (numbered, tagged chunks with source ids so the model can cite), and lower temperature. The diagnostic order matters: check retrieval first, because most bugs live there. A good rule of thumb is that if a human reading only the retrieved context could answer the question, the problem is generation; if not, the problem is retrieval.