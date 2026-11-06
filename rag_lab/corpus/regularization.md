---
title: Regularization (L1 vs L2)
topic: ml-fundamentals
difficulty: medium
---
# Question
What is regularization and what's the difference between L1 and L2?

# Key points
- Regularization adds a penalty to the loss to discourage large weights / complexity
- L1 (|w|) drives some weights exactly to zero → sparsity, feature selection
- L2 (w²) shrinks weights toward zero but rarely exactly to zero
- L1 is preferred when you suspect few features matter; L2 when all do but you want them small

# Reference answer
Regularization adds a penalty term to the loss so the model trades training fit for simpler weights. L1 (Lasso) adds sum of absolute weights; its gradient is constant, so it pushes small weights all the way to zero — giving sparse models and implicit feature selection. L2 (Ridge) adds sum of squared weights; its gradient shrinks with magnitude, so weights get small but not exactly zero. Choose L1 when you suspect only a few features matter, L2 when most carry signal but you want to bound them, and ElasticNet when you want both. In deep nets, L2 is often implemented as "weight decay," and dropout is a form of regularization that acts like an ensemble of subnetworks.