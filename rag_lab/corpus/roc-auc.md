---
title: ROC-AUC
topic: evaluation
difficulty: medium
---
# Question
What does ROC-AUC measure, and when is it misleading?

# Key points
- ROC curve: TPR (recall) vs FPR across all thresholds
- AUC = probability a random positive is scored higher than a random negative
- Threshold-independent — good for comparing models, not for picking a threshold
- Misleading under heavy imbalance: dominated by TN, can look good while PR is terrible

# Reference answer
The ROC curve plots true positive rate (recall) against false positive rate as you sweep the classification threshold. AUC — the area under it — has a clean interpretation: the probability that a random positive is scored higher than a random negative by the model. Because it averages over all thresholds, it's threshold-independent, which is useful for comparing models before committing to an operating point. Two caveats. First, it doesn't tell you which threshold to use — for that you look at the actual ROC curve at the operating point you care about. Second, under heavy class imbalance, ROC-AUC can look strong because the FPR denominator (TN + FP) is dominated by TNs — the model barely has to do better than "predict negative" to keep FPR low. Use PR-AUC (precision vs recall) instead when positives are rare.