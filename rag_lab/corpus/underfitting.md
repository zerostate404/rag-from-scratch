---
title: Underfitting
topic: ml-fundamentals
difficulty: easy
---
# Question
What is underfitting and how do you address it?

# Key points
- Defines underfitting as the model being too simple to capture the underlying pattern
- Identifies the signature: high training error AND high validation error
- Distinguishes from overfitting (both errors high, not just validation)
- Names at least one mitigation: more capacity, better features, train longer, reduce regularization

# Reference answer
Underfitting is when a model is too simple — or too heavily constrained — to capture the pattern in the data. Unlike overfitting, both training and validation error are high, so the model isn't even learning the training set well. Common causes are insufficient model capacity, under-trained (too few epochs or too low learning rate), overly aggressive regularization, or poor features that don't carry the signal. Fixes are the mirror image of overfitting fixes: increase model capacity, add or engineer better features, train longer, reduce regularization strength, or use a more expressive architecture. The key diagnostic is that training error is *also* high — if training error is low, you're not underfitting.