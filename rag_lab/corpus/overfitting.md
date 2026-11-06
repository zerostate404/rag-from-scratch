---
title: Overfitting
topic: ml-fundamentals
difficulty: easy
---
# Question
What is overfitting and how do you detect it?

# Key points
- Defines overfitting as memorizing training data (including noise), leading to poor generalization
- Identifies the classic signature: low training error + high validation error (a gap)
- Mentions at least one detection method: train/val gap, learning curves, or cross-validation
- Mentions at least one mitigation: regularization, dropout, early stopping, or more data

# Reference answer
Overfitting is when a model learns the training data too well — including its noise — so it performs poorly on unseen data. The classic detection signal is a large gap between training and validation performance: low training loss, high validation loss. Learning curves that diverge, or a validation score that drops sharply during cross-validation, are the same signal from different angles. Mitigation includes L1/L2 regularization, dropout, early stopping when validation loss stops improving, and getting more training data. The deeper issue is model capacity exceeding what the data can support — so the fix is either reduce the capacity or increase the data.