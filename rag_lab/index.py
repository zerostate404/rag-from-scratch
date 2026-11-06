"""Build retrieval indexes: embed all chunks once, save to disk."""

import json
import time
from pathlib import Path
# REPLACE with this
from llm import client, EMBED_MODEL
import numpy as np

from chunking import parse_note, chunk_fixed, chunk_structure


INDEX_DIR = Path("indexes")
BATCH_SIZE = 16


def embed_batch(texts):
    """Embed a batch of texts and return a (n, 768) numpy array."""
    r = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return np.array([d.embedding for d in r.data], dtype=np.float32)


def build_index(chunks, strategy):
    """Embed all chunks for one strategy and save .npy + .json to disk."""
    texts = [f"search_document: {c['text']}" for c in chunks]

    print(f"\n[{strategy}] embedding {len(texts)} chunks "
          f"in batches of {BATCH_SIZE}...")

    t0 = time.perf_counter()
    vectors = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i:i + BATCH_SIZE]
        vectors.append(embed_batch(batch))
        print(f"  batch {i // BATCH_SIZE + 1}: "
              f"{len(batch)} chunks embedded")
    elapsed = time.perf_counter() - t0

    vec_array = np.vstack(vectors)

    INDEX_DIR.mkdir(exist_ok=True)
    npy_path = INDEX_DIR / f"{strategy}.npy"
    json_path = INDEX_DIR / f"{strategy}.json"

    np.save(npy_path, vec_array)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"  shape: {vec_array.shape}")
    print(f"  total time: {elapsed:.1f}s "
          f"({elapsed / len(texts) * 1000:.0f} ms/chunk)")
    print(f"  saved: {npy_path}  +  {json_path}")

    return vec_array, elapsed


def load_index(strategy):
    """Reload a saved index. Use this in retrieve.py — never re-embed."""
    npy_path = INDEX_DIR / f"{strategy}.npy"
    json_path = INDEX_DIR / f"{strategy}.json"
    vectors = np.load(npy_path)
    with open(json_path, encoding="utf-8") as f:
        chunks = json.load(f)
    return vectors, chunks


if __name__ == "__main__":
    notes = [parse_note(p) for p in sorted(Path("corpus").glob("*.md"))]
    print(f"Parsed {len(notes)} notes from corpus/")

    fixed_chunks = []
    structure_chunks = []
    for n in notes:
        fixed_chunks += chunk_fixed(n)
        structure_chunks += chunk_structure(n)

    print(f"Fixed chunks: {len(fixed_chunks)}")
    print(f"Structure chunks: {len(structure_chunks)}")

    build_index(fixed_chunks, "fixed")
    build_index(structure_chunks, "structure")

    # Sanity: reload both, verify shapes match
    print("\n" + "=" * 60)
    print("Verify reload")
    print("=" * 60)
    for strat in ("fixed", "structure"):
        v, c = load_index(strat)
        print(f"  {strat:<10} vectors={v.shape}  chunks={len(c)}  "
              f"match={v.shape[0] == len(c)}")