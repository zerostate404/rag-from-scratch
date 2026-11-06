---
title: Vanishing/Exploding Gradients
topic: training
difficulty: medium
---
# Question
What causes vanishing or exploding gradients, and how do you fix them?

# Key points
- Vanishing: gradients shrink through many layers/timesteps (sigmoid/tanh, deep chains, RNNs)
- Exploding: gradients grow exponentially (poor init, unstable recurrences)
- Fixes for vanishing: ReLU, residual connections, LSTM/GRU gates, careful init (Xavier/He), normalization
- Fixes for exploding: gradient clipping, careful init, lower LR

# Reference answer
Both come from multiplying many Jacobians together in deep or recurrent networks. If the Jacobian's singular values are < 1, gradients vanish — sigmoid/tanh saturate, and early layers get almost no signal. If > 1, they explode. Vanishing fixes: replace sigmoid/tanh with ReLU (non-saturating), add residual connections so gradients can flow around blocks, use gated RNNs (LSTM/GRU) with learnable gates that control flow, and initialize with Xavier/He schemes that keep activation variance stable. Layer normalization also helps. Exploding fixes: gradient clipping (rescale gradients above a threshold), more careful init, and — often overlooked — lowering the learning rate. Modern transformers rely on residuals + layernorm + careful init, which is why they train deep without vanishing.