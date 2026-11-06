---
title: Bias-Variance Tradeoff
topic: ml-fundamentals
difficulty: medium
---
# Question
Explain the bias-variance tradeoff.

# Key points
- Bias = error from overly simple assumptions (systematic, underfitting)
- Variance = error from sensitivity to training data (overfitting)
- Total error = bias² + variance + irreducible error
- Tradeoff: reducing one typically increases the other; optimal complexity minimizes total
- Modern caveat: with over-parameterized models (deep nets), double descent can break the classic U-curve

# Reference answer
Bias is error from wrong assumptions — a linear model fitting a nonlinear pattern has high bias. Variance is error from sensitivity to the training data — a deep tree that changes shape with every sample has high variance. Expected total error decomposes as bias² + variance + irreducible noise. Classic theory says there's a sweet spot: too simple → high bias (underfitting), too complex → high variance (overfitting). The practical takeaway is you diagnose which is dominant and fix accordingly. Modern caveat: heavily over-parameterized networks can exhibit "double descent" — test error decreases past the interpolation threshold — so the classic U-curve doesn't always apply. Still, the decomposition is the right diagnostic frame.