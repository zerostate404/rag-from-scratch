---
title: Cosine Similarity
topic: rag
difficulty: easy
---
# Question
What is cosine similarity and why use it for embeddings?

# Key points
- cos(a, b) = (a·b) / (‖a‖ · ‖b‖)
- Range −1 to 1; for text embeddings usually 0 to 1
- Measures angle (direction), not magnitude — robust to vector length
- Faster alternative when vectors are normalized: dot product = cosine
- Other metrics: Euclidean (magnitude-sensitive), dot product (biased by magnitude)

# Reference answer
Cosine similarity is the cosine of the angle between two vectors: (a·b)/(‖a‖·‖b‖). It ranges from −1 (opposite) through 0 (orthogonal) to 1 (identical direction). For text embeddings it's usually 0 to 1, because text vectors cluster in one region of the space. It's the standard metric because it ignores *magnitude* — a short sentence and a long paragraph with the same meaning have different vector lengths but similar directions, and cosine captures that. If both vectors are unit-normalized (many embedding models return normalized vectors), cosine reduces to just the dot product, which is faster and what vector databases compute. Alternatives: Euclidean distance is magnitude-sensitive and can mislead when vectors differ in length for reasons unrelated to meaning; dot product is fine but biased toward longer vectors unless you normalize first. Whatever metric you use, be consistent — don't rank by cosine and then filter by Euclidean.