---
title: Chunking Strategies
topic: rag
difficulty: medium
---
# Question
What are the trade-offs in chunking for RAG?

# Key points
- Small chunks: precise retrieval, but may lack context and split sentences/ideas
- Large chunks: more context, but the embedding blurs multiple ideas into one vector
- Common strategy: split on semantic boundaries (headings, paragraphs), overlap 10–20%
- Metadata (section, position) helps filter and reassemble
- Fixed-size token chunking is easy but cuts mid-sentence and mid-idea

# Reference answer
Chunking is the split of your corpus into retrievable units, and it's the highest-leverage knob in RAG. Small chunks (e.g. 200 tokens) embed tightly — the vector represents one focused idea — so retrieval is precise, but the retrieved chunk may lack the context the LLM needs. Large chunks (e.g. 1500 tokens) preserve context but the embedding averages over multiple ideas, so retrieval gets fuzzier. Standard practice: split on semantic boundaries — markdown headings, paragraphs, sections — rather than fixed token counts, because fixed-size chunking cuts mid-sentence and mid-idea. Overlap chunks by 10–20% so a boundary sentence appears in both neighbours. Store metadata (source, heading, position) so you can filter, cite, or reassemble. For markdown notes with clear `# Question` / `# Key points` / `# Reference answer` headers, split on headers first, then token-split only if a section is too long.