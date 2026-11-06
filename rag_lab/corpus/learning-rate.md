---
title: Learning Rate
topic: training
difficulty: easy
---
# Question
What role does the learning rate play in training?

# Key points
- Controls the step size of each weight update
- Too high → overshoot, divergence, or oscillating loss
- Too low → slow convergence, may get stuck in poor local minima
- Common strategies: warmup, decay schedules, adaptive optimizers (Adam), learning-rate finders

# Reference answer
In gradient descent, the learning rate — also called step size — scales each weight update, effectively how far you step in the negative-gradient direction.Too large and you overshoot the minimum: loss oscillates, spikes, or diverges. Too small and training crawls, burns budget, and may get stuck in poor regions. Standard practice is warmup (small LR for the first few hundred steps so early gradients don't blow up the weights), then a decay schedule (cosine, step, or linear) so the LR is large early and small late when you're polishing. Adaptive optimizers like Adam maintain per-parameter learning rates based on gradient history, which reduces sensitivity to the initial choice but doesn't eliminate the need to tune a base LR.