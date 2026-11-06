"""RAG generation: retrieve context, build prompt, call the LLM."""

from retrieve import retrieve
from llm import client, CHAT_MODEL


SYSTEM = (
    "Answer the question using ONLY the provided context chunks. "
    "Cite each claim with the source id in square brackets, e.g. [S1]. "
    "If the context does not contain enough information to answer, "
    "respond with exactly: 'The provided context does not cover this topic.' "
    "Do not use your own knowledge to fill gaps."
)


def build_context(results):
    """Format retrieved chunks as [S1]...[Sk] blocks with source labels."""
    lines = []
    for r in results:
        lines.append(f"[S{r['rank']}] (source: {r['source']})\n{r['text']}")
    return "\n\n".join(lines)


def generate(query, strategy="structure", k=3, temperature=0.2):
    """Retrieve → build prompt → generate. Returns dict with text + diagnostics."""
    results = retrieve(query, strategy, k=k, only_reference=True)
    context = build_context(results)

    messages = [
        {"role": "system", "content": SYSTEM},
        {
            "role": "user",
            "content": f"Context:\n\n{context}\n\nQuestion: {query}",
        },
    ]

    r = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=temperature,
    )

    return {
        "text": r.choices[0].message.content,
        "input_tokens": r.usage.prompt_tokens,
        "output_tokens": r.usage.completion_tokens,
        "finish_reason": r.choices[0].finish_reason,
        "retrieved": results,
    }


if __name__ == "__main__":
    queries = [
        # answerable — should cite [S1] and give the key facts
        "What is overfitting and how do you detect it?",

        # low-overlap paraphrase — should still work
        "how do I make an LLM return reliable JSON?",

        # unanswerable — should say "not covered"
        "How does a Kubernetes Deployment differ from a ReplicaSet?",
    ]

    for q in queries:
        print("\n" + "=" * 70)
        print(f"Q: {q}")
        print("=" * 70)

        out = generate(q)

        print(f"finish_reason={out['finish_reason']}  "
              f"input_tokens={out['input_tokens']}  "
              f"output_tokens={out['output_tokens']}")

        print(f"\nRetrieved {len(out['retrieved'])} chunks:")
        for r in out["retrieved"]:
            print(f"  [S{r['rank']}] {r['score']:.3f}  {r['source']}")

        print(f"\nAnswer:\n{out['text']}")