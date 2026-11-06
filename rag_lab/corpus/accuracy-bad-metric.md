---
title: When Accuracy Is a Bad Metric
topic: evaluation
difficulty: easy
---
# Question
When is accuracy a bad metric, and what should you use instead?

# Key points
- Bad under class imbalance: a "predict majority class" baseline can have high accuracy while being useless
- Example: 99:1 imbalance → always-predict-negative scores 99%
- Better: precision/recall, F1, ROC-AUC, PR-AUC, per-class metrics, confusion matrix
- Also bad when error costs are asymmetric (a missed diagnosis ≠ a false alarm)

# Reference answer
Accuracy treats every correct prediction as equally valuable, which is wrong in two common situations. First, class imbalance: with a 99:1 negative:positive split, a model that always predicts negative gets 99% accuracy while catching zero positives — the number is technically true and completely useless. Use precision/recall, F1, PR-AUC, or the confusion matrix instead. Second, asymmetric error costs: in a medical screening task a false negative (missed cancer) is far worse than a false positive (extra test), so you want high recall even at the cost of precision. In those cases the relevant question isn't "how often is it right?" but "how often does it fail in the way that matters?" — which is a per-class, per-error-type metric, not a global rate.