---
title: Vector Embeddings
topic: rag
difficulty: easy
---
# Question
What is a vector embedding?

# Key points
- A dense numeric vector (e.g. 768-dim) representing the meaning of text
- Produced by an embedding model trained so similar meanings have similar vectors
- Similarity is measured with cosine (or dot product / Euclidean)
- Encodes topic/semantic similarity, not correctness or truth
- Same model must embed query and documents — mixing models gives meaningless similarities

# Reference answer
A vector embedding is a fixed-length dense numeric vector that represents text — a sentence, paragraph, or document — in a space where semantically similar text is close together. A 768-dim embedding is 768 floats; no individual dimension has meaning, but the vector's *position* encodes the meaning. The model is trained contrastively: pairs that mean similar things are pulled together, unrelated pairs pushed apart. Similarity between two embeddings is usually measured with cosine similarity — the cosine of the angle between them — which ranges roughly 0 to 1 for text. Two properties matter operationally: (1) embeddings capture topical/semantic similarity but **not correctness** — a wrong but on-topic answer can embed as close to a right answer as a correct paraphrase does; (2) query and documents must use the *same* embedding model, because vectors from different models live in different spaces with no meaningful relationship.