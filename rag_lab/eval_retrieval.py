"""Retrieval eval: hit@k, MRR, rank-1 misses, section distribution."""

from collections import Counter

from retrieve import retrieve


EVAL_SET = [
    # --- high-overlap (canonical phrasing) ---
    ("What is overfitting and how do you detect it?", "overfitting.md"),
    ("What's the difference between L1 and L2 regularization?", "regularization.md"),
    ("How does gradient descent update weights?", "gradient-descent.md"),
    ("What is the F1 score and when should I use it?", "f1-score.md"),
    ("What does ROC-AUC measure?", "roc-auc.md"),
    ("How does a RAG pipeline work end to end?", "what-is-rag.md"),
    ("What is chunking and how should I split documents?", "chunking-strategies.md"),
    ("What does temperature do in LLM sampling?", "temperature.md"),
    ("What is a vector embedding?", "vector-embeddings.md"),
    ("What is prompt injection and how do you defend against it?", "prompt-injection.md"),

    # --- low-overlap paraphrases ---
    ("why does my model do worse on new data than on training data?", "overfitting.md"),
    ("what's the step size in gradient descent called?", "learning-rate.md"),
    ("how do I make an LLM return reliable JSON?", "structured-output.md"),
    ("how does the model know when to call my function?", "tool-calling.md"),
    ("why does my RAG pipeline give bad answers?", "when-rag-fails.md"),
]


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def hit_at_k(strategy, k, use_filter=False):
    hits = 0
    for query, expected in EVAL_SET:
        results = retrieve(query, strategy, k=k, only_reference=use_filter)
        if any(r["source"] == expected for r in results):
            hits += 1
    return hits / len(EVAL_SET)


def mrr(strategy, k_max=10, use_filter=False):
    total = 0.0
    for query, expected in EVAL_SET:
        results = retrieve(query, strategy, k=k_max, only_reference=use_filter)
        for r in results:
            if r["source"] == expected:
                total += 1.0 / r["rank"]
                break
    return total / len(EVAL_SET)


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------

def rank1_misses(strategy, use_filter=False):
    tag = f"{strategy}, filter={use_filter}"
    print(f"\n--- rank-1 misses ({tag}) ---")
    n = 0
    for query, expected in EVAL_SET:
        results = retrieve(query, strategy, k=3, only_reference=use_filter)
        if results[0]["source"] != expected:
            n += 1
            print(f"\n  MISS @ rank 1: {query!r}")
            print(f"    expected: {expected}")
            for r in results[:3]:
                print(f"    got [{r['rank']}] {r['score']:.3f}  "
                      f"{r['source']} ({r['section']})")
    if n == 0:
        print("  (no rank-1 misses)")


def section_distribution(strategy, use_filter=False):
    tag = f"{strategy}, filter={use_filter}"
    c = Counter()
    for query, _ in EVAL_SET:
        r = retrieve(query, strategy, k=1, only_reference=use_filter)[0]
        c[r["section"]] += 1
    print(f"\n--- rank-1 section distribution ({tag}) ---")
    for section, n in c.most_common():
        print(f"  {section:<20} {n}/{len(EVAL_SET)}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    n_lowoverlap = sum(1 for q, _ in EVAL_SET if q[0].islower())
    print(f"Eval set: {len(EVAL_SET)} queries ({n_lowoverlap} low-overlap)")

    # --- headline table ---
    print()
    header = f"{'strategy':<22}{'hit@1':>8}{'hit@3':>8}{'hit@5':>8}{'MRR':>8}"
    print(header)
    print("-" * len(header))

    configs = [
        ("fixed",      False),
        ("structure",  False),
        ("structure",  True),   # filtered — what Step 5 will use
    ]
    for strat, filt in configs:
        label = f"{strat}{' (filtered)' if filt else ''}"
        h1 = hit_at_k(strat, 1, use_filter=filt)
        h3 = hit_at_k(strat, 3, use_filter=filt)
        h5 = hit_at_k(strat, 5, use_filter=filt)
        m  = mrr(strat, use_filter=filt)
        print(f"{label:<22}{h1:>8.2f}{h3:>8.2f}{h5:>8.2f}{m:>8.3f}")

    # --- diagnostics — only for the two configurations we still care about ---
    rank1_misses("fixed", use_filter=False)
    rank1_misses("structure", use_filter=True)
    section_distribution("structure", use_filter=False)
    section_distribution("structure", use_filter=True)