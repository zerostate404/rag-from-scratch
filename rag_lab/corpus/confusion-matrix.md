---
title: Confusion Matrix
topic: evaluation
difficulty: easy
---
# Question
What is a confusion matrix and what can you read from it?

# Key points
- 2×2 (for binary) table of predicted vs actual: TP, FP, FN, TN
- Every classification metric (precision, recall, F1, accuracy, specificity) is a ratio of these four cells
- Reveals error *types* not just rates: is the model missing positives (FN) or over-firing (FP)?
- Extends to NxN for multiclass — each class has one-vs-rest cells

# Reference answer
A confusion matrix tabulates predictions against true labels. For binary classification it's 2×2: true positives, false positives, false negatives, true negatives. Everything else is a derived ratio: accuracy = (TP+TN)/N, precision = TP/(TP+FP), recall = TP/(TP+FN), specificity = TN/(TN+FP). The value of looking at the matrix — rather than just a rate — is that it tells you *which kind of error* dominates. If you only looked at accuracy on an imbalanced dataset (99% negative), a model that predicts negative always scores 99% — but the confusion matrix immediately shows FN = all positives, i.e. it doesn't work. For multiclass, you build an N×N matrix and each class gets its own precision/recall computed one-vs-rest.