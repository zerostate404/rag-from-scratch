---
title: Tool Calling
topic: prompting
difficulty: medium
---
# Question
How does tool calling / function calling work in LLM APIs?

# Key points
- You define a tool in three parts that must agree on the name: the function, a JSON schema describing it, and a registry mapping name→function
- The model doesn't execute anything — it returns a structured `tool_calls` request with arguments
- You execute the function, append the result as a `tool` role message with matching `tool_call_id`, and call the model again
- The second call should NOT pass `tools=` (or you risk another tool call instead of a final answer)

# Reference answer
Tool calling is a two-turn protocol. First you describe available tools to the model as JSON schemas — name, description, parameter schema. On the user turn, the model can either produce text or return a `tool_calls` list, each with a name and an arguments string. It does not execute anything; it just requests. Your code parses the arguments, looks up the function by name, executes it, then appends two messages to the conversation: the assistant message that contains the tool_calls request, and a `tool` role message with the result and the matching `tool_call_id`. Then you call the model again — without passing `tools=`, because the second call's job is to turn the tool result into user-facing text, and passing tools again invites a second tool call instead of an answer. The message protocol is strict: skipping the assistant message means the model sees a tool result with no idea what request it answers; skipping the tool message means the model is waiting for a response that never arrives. The tool_call_id is how each result is matched to its request when there are parallel calls. Common failure modes cluster into three groups. First, the model emits a fake tool call as text — `{"name": "get_question", "parameters": {...}}` written into the response content instead of a structured tool_calls request. Second, the model invents arguments the schema disallows (missing required fields, extra fields, wrong types), which should be caught by your execute-and-validate wrapper. Third, the model hallucinates a tool result — it claims "the tool returned X" when no tool was called or the tool returned Y. All three indicate the model's understanding of the protocol is shallow; the defenses are a strict system prompt, schema validation, and a two-call pattern that never invites ambiguity about what phase it is in.