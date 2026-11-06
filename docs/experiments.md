╰──# python3 02_params.py

--- temperature=0.0 ---
0 "Code Your Future in 12 Weeks" (0.44s)
1 "Code Your Future in 12 Weeks" (0.39s)
2 "Code Your Future in 12 Weeks" (0.4s)

--- temperature=1.0 ---
0 "Code your future in 12 weeks or less" (0.46s)
1 Here is a one-line tagline for a coding bootcamp:

"Write your future, line by line." (0.89s)
2 "Learn to code, launch your future." (0.39s)

--- temperature=1.0, seed=42 ---
0 Here is a one-line tagline for a coding bootcamp:

"Gain the skills to code your future in as little as 12 weeks." (1.19s)
1 Here is a one-line tagline for a coding bootcamp:

"Gain the skills to code your future in as little as 12 weeks." (1.14s)
2 Here is a one-line tagline for a coding bootcamp:

"Gain the skills to code your future in as little as 12 weeks." (1.15s)

--- max_tokens=5 ---
Text:  'A vector embedding is a'
Finish reason:  length
Output tokens:  5

--- No System Prompt ---
The perils of overfitting!

**What is overfitting?**

Overfitting is a phenomenon that occurs in machine learning models when a model is too complex and learns the noise or randomness in the training data, rather than the underlying patterns or relationships that explain the data. In other words, the model becomes too specialized to the training data and loses its ability to generalize well to new, unseen data.

**Symptoms of overfitting:**

1. **High training accuracy**: The model performs well on the training data, but the accuracy on new, unseen data (test or validation set) is much lower.
2. **Large model size**: Overfitting often occurs in models with a large number of parameters, which can lead to over-regularization and under-smoothing of the model.
3. **Rapid improvement in training accuracy**: At first, the model improves its performance on the training data, but then it starts to overfit and the improvement slows down.

**Causes of overfitting:**

1. **Model complexity**: Models with too many parameters or layers are more prone to overfitting.
2. **Small training set**: Overfitting can occur when the model is trained on a small training set, making it difficult for the model to generalize to larger datasets.
3. **Imbalanced data**: When the training data is imbalanced (i.e., one class or label has a significantly larger number of instances), the model may overfit to the majority class.
4. **High-dimensional data**: Models may overfit when dealing with high-dimensional data, as the model may start to fit the noise in the data rather than the underlying structure.

**Examples of overfitting:**

1. A decision tree model that overfits to the noise in the data and becomes too specialized to the training data.
2. A neural network that has too many layers or too many neurons in each layer, resulting in over-regularization and under-smoothing.
3. A regression model that overfits the relationship between the response variable and one or more predictor variables, resulting in poor predictions on new, unseen data.

**Solutions to overfitting:**

1. **Regularization**: Techniques like L1 and L2 regularization, dropout, and early stopping can help prevent overfitting by penalizing large weights and reducing the capacity of the model.
2. **Model simplicity**: Using simpler models or reducing the number of parameters can help prevent overfitting.
3. **Data augmentation**: Increasing the size of the training set through data augmentation techniques like rotation, scaling, and flipping can help generalization.
4. **Ensemble methods**: Combining multiple models can help improve generalization and prevent overfitting.
5. **Use techniques like cross-validation to evaluate model performance on unseen data**.

I hope this explanation helps you understand overfitting!

--- With System Prompt ---
Overfitting occurs when a model is too complex and learns the training data so well that it starts to fit the noise or random fluctuations in the data, thereby failing to generalize well to new, unseen data. Effective regularization techniques, such as L1 and L2 regularization, dropout, and early stopping, are commonly used to combat overfitting. 

Can you explain the difference between L1 and L2 regularization and provide an example of when to use each?

==================================================================================
Temp 0: 3 identical outputs, 0.4s each. Near-deterministic, which is what you want for evals.

Temp 1: 3 different taglines. One also added a “Here is a one-line tagline...” preamble, so small models get chatty.

Temp 1 + seed=42: 3 identical outputs. So a seed makes high-temperature sampling reproducible, and you can debug a weird output by replaying it. Reproducible doesn’t mean good, though: that run kept the chatty preamble.

max_tokens=5: 'A vector embedding is a' with finish_reason: length. The answer was cut mid-sentence and nothing raised an error, so the only signal is that field. Always check it.

System prompt: it obeyed both rules (2 sentences plus a follow-up question), while the no-system-prompt answer was a long wall of headers. You saw this model miss “5 words” earlier, so obedience is inconsistent. Never assume it, and test it.

==================================================================================
╰──# python3 learning/03_structured_output.py

with system prompt:
SYSTEM = (
    "You are a strict technical interviewer. Reply with ONLY a JSON object with keys: "
    "score (integer 1-10), strengths (list of strings), weaknesses (list of strings), "
    "follow_up (string). No extra text."
)

1 score=6 strengths=['Identified key issue in machine learning', 'Simple and clear explanation'] weaknesses=['Lacked technical depth', 'Did not provide any mathematical or statistical explanation'] follow_up='Can you explain the concept of regularization and how it helps prevent overfitting?


The weakness it listed (“did not provide any mathematical or statistical explanation”) is something nobody asked for.

with system prompt:
SYSTEM1 = """
You are a fair and strict technical interviewer.

Evaluate the candidate's answer based on:
1. Technical correctness.
2. Relevance to the question.
3. Completeness relative to what the question asks.
4. Clarity and precision.

Important rules:
- Do not penalize concise answers if they adequately answer the question.
- Do not demand mathematical derivations, examples, or additional concepts
  unless the question explicitly requires them.
- Distinguish factual errors from missing optional details.
- Award scores proportionally to correctness and completeness.
- Provide specific, justified strengths and weaknesses.

Return ONLY a JSON object with:
score (integer 1-10),
strengths (list of strings),
weaknesses (list of strings),
follow_up (string).
"""

1 score=8 strengths=['Correctly identifies the core issue of overfitting', 'Provides a concise and clear explanation'] weaknesses=['Lacks technical specificity and detail', 'Does not mention regularization or other techniques to prevent overfitting'] follow_up='Can you give an example of a situation where overfitting occurs, and how regularization can help prevent it?'

==================================================================================
Run it with three answers: a good one, a clearly wrong one (“overfitting is when the model is too simple”), and gibberish (“banana”). Does the score make sense for each? (temp=0.2)

from importlib import import_module
from pydantic import BaseModel, Field, ValidationError

ask = import_module("01_ollama_basics").ask


class Feedback(BaseModel):
    score: int = Field(ge=1, le=10)
    strengths: list[str]
    weaknesses: list[str]
    follow_up: str


SYSTEM = (
    "You are a strict technical interviewer. Reply with ONLY a JSON object with keys: "
    "score (integer 1-10), strengths (list of strings), weaknesses (list of strings), "
    "follow_up (string). No extra text."
)

SYSTEM1 = """
You are a fair and strict technical interviewer.

Evaluate the candidate's answer based on:
1. Technical correctness.
2. Relevance to the question.
3. Completeness relative to what the question asks.
4. Clarity and precision.

Important rules:
- Do not penalize concise answers if they adequately answer the question.
- Do not demand mathematical derivations, examples, or additional concepts
  unless the question explicitly requires them.
- Distinguish factual errors from missing optional details.
- Award scores proportionally to correctness and completeness.
- Provide specific, justified strengths and weaknesses.

Return ONLY a JSON object with:
score (integer 1-10),
strengths (list of strings),
weaknesses (list of strings),
follow_up (string).
"""

def score_answer(question, answer, max_iters=3):
    prompt = f"Question: {question}\nCandidate answer: {answer}"
    for attempt in range(1, max_iters + 1):
        r = ask(
            prompt,
            system=SYSTEM1,
            temperature=0.2,
            response_format={"type": "json_object"},
        )

        try:
            return Feedback.model_validate_json(r["text"]), attempt
        except ValidationError as e:
            prompt += f"\n\nYour previous reply was invalid: {e}. Return corrected JSON only."
            

    raise ValueError("model never returned valid JSON")


if __name__ == "__main__":
    for ans in ("When a model memorizes training data and fails on new data.", "overfitting is when the model is too simple", "banana"):
        fb, tries = score_answer("What is overfitting?",
                                 ans)

        print(tries, fb, "\n")

╰──# python3 learning/03_structured_output.py
1 score=8 strengths=['Correctly identifies the core issue of overfitting', 'Concise and easy to understand'] weaknesses=['Lacks technical specificity and detail', 'Does not mention regularization or other common techniques to prevent overfitting'] follow_up='Can you explain why a model might memorize training data and how to prevent it?' 

1 score=4 strengths=['The candidate has a basic understanding of overfitting.'] weaknesses=["The answer is incomplete and doesn't accurately describe overfitting.", 'The statement is factually incorrect; overfitting typically occurs when a model is too complex, not too simple.'] follow_up='Can you explain what happens when a model is too complex and how it relates to overfitting?' 

Traceback (most recent call last):
  File "/home/kakarotbot/spectov-prep/learning/03_structured_output.py", line 65, in <module>
    fb, tries = score_answer("What is overfitting?",
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/kakarotbot/spectov-prep/learning/03_structured_output.py", line 60, in score_answer
    raise ValueError("model never returned valid JSON")
ValueError: model never returned valid JSON

==================================================================================

Embeddings Drill Results: nomic-embed-text
Kakarot · SpectoV AI Engineer Intern prep · November 5, 2026
Summary
• Problem 3 (right vs wrong answers): embeddings give a weak signal. They reject nonsense clearly, but any single wrong answer can outscore a correct one, so they can gate relevance but cannot grade correctness.
• Problem 4 (retrieval): well above chance on 12 short docs and 9 single-label queries (hit@1 5/9, hit@3 7/9), but the right doc usually wins by a hair, and the failures are vocabulary mismatches.
• Decision: use embeddings for retrieval and relevance gating only, and test hybrid search and re-ranking on longer documents in Concept 6.
Problem 3: not a reliable grader
Setup: 4 right answers, 4 wrong answers, 2 nonsense answers, all embedded with nomic-embed-text (768 dimensions).
Comparison
Mean cosine
right vs right
0.635
wrong vs right
0.544
nonsense vs right
0.364
Gap (right-right minus wrong-right)
+0.090
• Wrong answers sit clearly above nonsense and a bit below correct ones, but the distributions overlap heavily.
• Four of the 16 wrong-vs-right pairs score at or above the correct-paraphrase mean. The worst is "The model has not trained for enough epochs" (an underfitting answer) at 0.74 against R3.
• Frame effect (hypothesis, n=1 sentence): "The model is too simple." scores 0.67 and 0.63 against the two right answers that start with "The model", and 0.42 and 0.51 against the two that don't.
• Correction to an earlier claim: the first control (wrong answer scoring 0.668 against a right answer) was partly a sentence-frame effect, so "wrong answers look as close as right ones" was overstated. The design conclusion still holds: embeddings can reject nonsense but cannot reliably judge correctness.
Problem 4: retrieval over 12 docs, 9 queries
One best-matching doc per query, so hit@1 and hit@3 are meaningful against chance.
Metric
Prefixed
No prefix
Chance
hit@1
5/9
5/9
8.3%
hit@3
7/9
7/9
25.0%
MRR
0.676
0.691
n/a
Mean gap (expected minus best other)
+0.038
+0.048
n/a
What worked: for "how do I stop my model from memorizing the training set?", the expected doc (Q5) ranked first in both modes, and Q7 ("Why does a model perform poorly on data it has never seen before?", almost no word overlap with the query) ranked second. That is the real semantic win.
Misses and near misses:
Query
Expected
Rank (prefixed / no prefix)
Top hit
how big should each update step be?
Q6 (learning rate)
9 / 8
Q5 (preventing overfitting)
my network is memorizing instead of learning
Q5
7 / 11
Q6 (learning rate)
what's the difference between a weight and a setting I choose before training?
Q2
3 / 2
Q3 (prefixed), Q6 (no prefix)
how do I detect that a model is overfitting?
Q0
2 / 2
Q5 (a defensible near miss)
• "My network is memorizing instead of learning" likely lost to the learning-rate doc because of the word "learning" (a guess; rankings alone cannot confirm it).
• "How big should each update step be?" is a true semantic miss: the model did not connect "update step size" to "learning rate".
• Prefixes: hit counts are identical, and prefixes helped one query and hurt two. With n=9 this is no evidence either way, so keep the documented prefix convention and recheck on the larger RAG eval.
What this changes for the build
Docs this short (8 to 12 words) give an embedding little to work with. In Concept 6 the 9-query set becomes a regression test for comparing:
1. Embeddings only (the current baseline)
2. Keyword search (BM25)
3. Hybrid (a combination of both)
4. Optionally, a re-ranker on top
The JD lists chunking, embeddings, vector search and re-ranking as responsibilities, so a table showing hit@1 before and after hybrid search is stronger evidence than a bullet point.
Cheap extra experiment: append aliases to each doc, for example "learning rate (step size, how large each weight update is)", and check whether Q6 climbs from 9th.
Log entry for docs/experiments.md
nomic-embed-text, 768-d. Right-right 0.635, wrong-right 0.544, nonsense-right 0.364 (n=4/4/2); 4/16 wrong answers outscored the correct-paraphrase mean, so embeddings are not usable as a correctness grader. Retrieval, 12 short docs, 9 single-label queries: hit@1 5/9, hit@3 7/9, MRR 0.68-0.69 (chance 8% / 25%); failures are vocabulary mismatches ("learning" pulled in the learning-rate doc; "update step" missed "learning rate"). Prefixes: no measurable difference (n=9). Decision: embeddings for retrieval and relevance gating only; test hybrid and re-ranking on longer docs.
Next step
Concept 6: RAG from scratch. It combines chunking, embeddings, retrieval, and a prompt that makes the model use the retrieved text.
==============================================

## Step 4b — section filtering

Raw structure strategy: hit@1=0.93, but 9/15 rank-1 wins were 'question' chunks.
The question is already in the generation prompt, so retrieving it wastes the
top context slot.

Fix: only_reference=True filter — restrict structure retrieval to
reference_answer chunks.

Filtered structure: hit@1=1.00, all rank-1 wins are reference_answer.
This is the retrieval configuration for Step 5 generation.

Corpus fix: learning-rate.md gained "step size" alias — the low-overlap
paraphrase "what's the step size in gradient descent called?" now hits
the correct note at rank 1. This was corpus engineering, not retrieval
improvement — the model was doing exactly what embeddings should do;
the corpus just lacked the vocabulary the query used.
==============================================
## Step 4 — final retrieval config for generation

Structure-aware + only_reference=True filter.
- hit@1 = 1.00, all 15 queries hit reference_answer at rank 1
- No question-chunk contamination
- Fixed strategy: 0.87, two misses are (a) overfitting/underfitting ambiguity — 
  fragmented chunks lose the train-vs-val-gap discriminator; (b) step-size — 
  even after alias fix, fragmentation prevents the three query terms from co-occurring.

Key finding: the alias fix (adding "step size" to learning-rate.md) helped 
structure (0.93 → 1.00) but NOT fixed (0.87 → 0.87). Same corpus, same edit, 
different outcome. Preserving semantic units is not just cleaner — it makes 
lexical aliases actually work.