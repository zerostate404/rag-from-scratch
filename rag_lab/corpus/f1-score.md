---
title: F1 Score
topic: evaluation
difficulty: easy
---
# Question
What is the F1 score and when would you use it?

# Key points
- Harmonic mean of precision and recall: 2PR / (P + R)
- Ranges 0–1; high only when both precision and recall are high
- Harmonic mean punishes imbalance — a model with P=1, R=0 has F1=0
- Use when classes are imbalanced and you care about both types of error

# Reference answer
F1 is the harmonic mean of precision and recall: 2PR/(P+R). It's used when classes are imbalanced and both false positives and false negatives matter, and you want a single number that can't be gamed by over-optimizing one at the expense of the other. The harmonic mean (vs arithmetic) is deliberate: it collapses toward the *worse* of the two, so a model with precision=1.0, recall=0.0 gets F1=0, not 0.5. F1 ignores true negatives entirely, which is a feature when TNs swamp the confusion matrix (e.g., rare event detection) — but a bug when specificity matters (e.g., medical screening where you also care about correctly clearing healthy patients). Variants: F-beta (β>1 weights recall higher), macro-F1 (per-class averaged, equal class weight), micro-F1 (global TP/FP/FN, dominated by majority class).