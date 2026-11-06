"""LLM client setup for rag_lab."""

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
CHAT_MODEL = "llama3.1-rag"          # num_ctx=5120, num_gpu=99
EMBED_MODEL = "nomic-embed-text"