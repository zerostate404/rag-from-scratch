---
title: Temperature
topic: prompting
difficulty: easy
---
# Question
What does temperature do in LLM sampling?

# Key points
- Scales logits before softmax: p_i ∝ exp(z_i / T)
- T < 1 sharpens the distribution → more deterministic, closer to argmax
- T > 1 flattens it → more diverse, more likely to pick lower-probability tokens
- T = 0 (or very small) ≈ greedy; not literally 0 in most APIs but effectively deterministic
- Trade-off: low T for correctness/extraction, high T for creativity; high T also increases hallucination

# Reference answer
Temperature rescales the logits before softmax: p_i ∝ exp(z_i / T). At T=1 the distribution is the model's natural output. Lower T sharpens it — high-probability tokens dominate, output gets more deterministic and repetitive. Higher T flattens it — low-probability tokens get relatively more likely, output gets more diverse and surprising. Practically: use low T (0–0.3) for extraction, structured output, and anything where you want reproducible answers; use mid T (0.7) for chat; use higher T (0.9–1.2) for brainstorming and creative writing. High T is *not* free — it increases hallucination, because sampling from the tails means picking tokens the model is unsure about. Temperature also interacts with `top_p` (nucleus sampling), which truncates the distribution — many APIs recommend tuning one and leaving the other at default.