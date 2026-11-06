---
title: Gradient Descent
topic: training
difficulty: easy
---
# Question
How does gradient descent update weights?

# Key points
- Computes gradient of the loss with respect to each parameter
- Updates weight in the opposite direction of the gradient: w ← w - lr * ∇L
- Learning rate controls step size
- Variants: batch (full dataset), stochastic (one sample), mini-batch (compromise)

# Reference answer
Gradient descent iteratively updates each weight in the direction that most decreases the loss. At each step you compute the gradient of the loss with respect to the weights — the direction of steepest ascent — and step in the opposite direction, scaled by a learning rate: w ← w − lr · ∇L(w). Batch gradient descent uses the full dataset per step (accurate but slow); stochastic GD uses one sample (noisy but fast); mini-batch is the standard compromise — accurate enough, fast enough, and friendly to GPU parallelism. The learning rate is critical: too large overshoots or diverges, too small crawls. Adaptive optimizers like Adam adjust the effective rate per-parameter using running statistics of past gradients.