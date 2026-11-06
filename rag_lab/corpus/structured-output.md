---
title: Structured Output / JSON Mode
topic: prompting
difficulty: easy
---
# Question
How do you get reliable structured output from an LLM?

# Key points
- Define the schema (Pydantic or JSON Schema) — the shape you want
- Instruct the model with the schema in the prompt, explicitly asking for JSON only
- Enable JSON mode (`response_format={"type": "json_object"}`) — guarantees syntactic validity
- Validate the response against the schema (Pydantic); retry with the validation error on mismatch
- JSON mode guarantees syntax, not shape — schema validation is still required

# Reference answer
Reliable structured output is four layers stacked. First, define the schema — Pydantic models are the cleanest because the same class validates and documents. Second, put the schema in the system prompt and explicitly say "return ONLY JSON with these keys, no extra text." Third, enable JSON mode — `response_format={"type": "json_object"}` in OpenAI-compatible APIs — which forces the model to emit syntactically valid JSON. Fourth, *validate* the response against the schema: JSON mode guarantees the syntax, not the shape, so the model can still return `{"score": "seven"}` when you asked for `score: int`. On validation failure, append the error message back to the prompt and retry — up to 2–3 times. This converts "the model got it wrong" into "the model sees exactly what it did wrong and tries again." Without JSON mode, first-try success rates on local models drop from ~100% to ~30%.