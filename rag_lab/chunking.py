"""Parse and chunk corpus notes for RAG indexing."""

import re
from pathlib import Path


def parse_note(path):
    """Parse a corpus markdown note into structured fields."""
    text = Path(path).read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError(f"No frontmatter in {path}")
    frontmatter_raw, body = m.group(1), m.group(2)

    meta = {}
    for line in frontmatter_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()

    sections = {}
    current_header = None
    current_lines = []
    for line in body.splitlines():
        if line.startswith("# "):
            if current_header is not None:
                sections[current_header] = "\n".join(current_lines).strip()
            current_header = line[2:].strip().lower()
            current_lines = []
        else:
            current_lines.append(line)
    if current_header is not None:
        sections[current_header] = "\n".join(current_lines).strip()

    key_points = [
        line[2:].strip()
        for line in sections.get("key points", "").splitlines()
        if line.strip().startswith("- ")
    ]

    return {
        "title": meta.get("title", ""),
        "topic": meta.get("topic", ""),
        "difficulty": meta.get("difficulty", ""),
        "question": sections.get("question", ""),
        "key_points": key_points,
        "reference_answer": sections.get("reference answer", ""),
        "source": Path(path).name,
    }


# ---------------------------------------------------------------------------
# Strategy A — fixed-size word windows
# ---------------------------------------------------------------------------

def chunk_fixed(note, chunk_size=100, overlap=20):
    """Split the whole note body into fixed-size windows with overlap."""
    full_text = " ".join([
        note["question"],
        " ".join(note["key_points"]),
        note["reference_answer"],
    ])
    words = full_text.split()
    stride = chunk_size - overlap
    chunks = []
    i = 0
    idx = 0
    while i < len(words):
        chunk_text = " ".join(words[i:i + chunk_size])
        chunks.append({
            "text": chunk_text,
            "source": note["source"],
            "title": note["title"],
            "section": "fixed",
            "chunk_num": idx,
            "strategy": "fixed",
        })
        idx += 1
        if i + chunk_size >= len(words):
            break
        i += stride
    return chunks


# ---------------------------------------------------------------------------
# Strategy B — structure-aware, one chunk per section
# ---------------------------------------------------------------------------

def chunk_structure(note):
    """Split on the note's own section headers."""
    sections = [
        ("question", note["question"]),
        ("key_points", "\n".join(f"- {p}" for p in note["key_points"])),
        ("reference_answer", note["reference_answer"]),
    ]
    chunks = []
    for idx, (name, content) in enumerate(sections):
        if not content.strip():
            continue
        chunks.append({
            "text": content,
            "source": note["source"],
            "title": note["title"],
            "section": name,
            "chunk_num": idx,
            "strategy": "structure",
        })
    return chunks


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------

def stats(chunks, label):
    lengths = [len(c["text"].split()) for c in chunks]
    print(f"\n[{label}]")
    print(f"  chunk count: {len(chunks)}")
    print(f"  avg length:  {sum(lengths) / len(lengths):.1f} words")
    print(f"  min length:  {min(lengths)} words")
    print(f"  max length:  {max(lengths)} words")


if __name__ == "__main__":
    notes = [parse_note(p) for p in sorted(Path("corpus").glob("*.md"))]
    print(f"Parsed {len(notes)} notes")

    fixed_chunks = []
    structure_chunks = []
    for n in notes:
        fixed_chunks += chunk_fixed(n)
        structure_chunks += chunk_structure(n)

    stats(fixed_chunks, "Strategy A — fixed window (100 words, 20 overlap)")
    stats(structure_chunks, "Strategy B — structure-aware")

    # Sample: the two long notes, both strategies
    print("\n" + "=" * 70)
    print("SAMPLE — when-rag-fails.md, both strategies")
    print("=" * 70)

    rag_note = next(n for n in notes if n["source"] == "when-rag-fails.md")

    print("\n[FIXED] chunks for this note:")
    for c in chunk_fixed(rag_note):
        print(f"  chunk {c['chunk_num']}: {len(c['text'].split())} words")
        print(f"    {c['text'][:120]}...")

    print("\n[STRUCTURE] chunks for this note:")
    for c in chunk_structure(rag_note):
        print(f"  chunk {c['chunk_num']} ({c['section']}): {len(c['text'].split())} words")
        print(f"    {c['text'][:120]}...")