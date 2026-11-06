"""Retrieve top-k chunks for a query. Never re-embeds the corpus."""

import numpy as np

from index import load_index
from llm import client, EMBED_MODEL


def embed_query(query):
    """Embed a single query with the search_query: prefix."""
    r = client.embeddings.create(model=EMBED_MODEL, input=[f"search_query: {query}"])
    return np.array(r.data[0].embedding, dtype=np.float32)


def retrieve(query, strategy, k=5, only_reference=False):
    """
    Return the top-k chunks for `query`.

    only_reference=True filters to reference_answer chunks only
    (structure strategy only) — used when feeding retrieval into
    generation, so the LLM gets *answers*, not the question echoed back.
    """
    vectors, chunks = load_index(strategy)

    if only_reference and strategy == "structure":
        keep = [i for i, c in enumerate(chunks)
                if c["section"] == "reference_answer"]
        vectors = vectors[keep]
        chunks = [chunks[i] for i in keep]

    qv = embed_query(query)
    norms = np.linalg.norm(vectors, axis=1) * np.linalg.norm(qv)
    scores = (vectors @ qv) / norms

    top_idx = np.argsort(-scores)[:k]
    return [
        {
            "rank": rank + 1,
            "score": float(scores[i]),
            "source": chunks[i]["source"],
            "section": chunks[i]["section"],
            "text": chunks[i]["text"],
            "chunk_num": chunks[i]["chunk_num"],
        }
        for rank, i in enumerate(top_idx)
    ]