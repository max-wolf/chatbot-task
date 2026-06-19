# Semantic Search Chatbot for Bookshop

## Running the project

### Setup
- Create and activate a virtual environment
- Install dependencies from `requirements.txt`

### Run modes

Normal mode:
```bash
python main.py
```

Debug mode:
```bash
python main.py --debug
```

---

## Matching approach

Semantic search is used as the primary retrieval method, combined with preprocessing.

### How it works
- User enters a question
- Query is preprocessed:
  - Lowercase normalisation
  - Slang expansion (u → you, pls → please)
  - Stopword removal ("the", "it", etc)
  - Deduplication
  - Synonym group expansion (append-only)
- Query is embedded using a transformer model
- Compared against precomputed FAQ embeddings
- Top 2 matches are retrieved
- Final decision uses:
  - Similarity threshold
  - Gap threshold (top-1 vs top-2)

### Why this approach was chosen
- Handles paraphrased user input effectively
- Reduces manual rule engineering compared to keyword matching
- No LLM required (no runtime cost or API dependency)
- Works well for small datasets (20 FAQs, fast inference)
- Captures semantic meaning rather than exact wording
- Lower hallucination risk compared to generative models

---

## Drawbacks

- Can confuse closely related intents (hence gap threshold mitigation)
- Requires careful threshold tuning (not optimised here)
- Less expressive than LLM-based reasoning and responses

---

## Handling “no good answer” cases

Two-layer confidence filtering is used:

### 1. Absolute confidence threshold
- If best similarity score is below a fixed threshold (e.g. 0.45)
- The system refuses to answer

Purpose:
- Prevents weak semantic matches being treated as valid
- Reduces incorrect or misleading responses

---

### 2. Relative ambiguity check (gap analysis)
- Compute difference between top-1 and top-2 scores
- If the gap is small, the result is treated as ambiguous

Purpose:
- Avoids selecting between nearly identical candidates
- Reduces unstable or “coin-flip” behaviour

---

### 3. Fallback response

If either check fails:

```
Sorry, I don't know that one — please ask a member of staff.
```

Priority is correctness over guessing.

---

## Tradeoffs

### Accuracy
- Strong at paraphrased queries
- Weakness in closely related intents without fine-tuning

### Latency
- Very fast inference (single embedding + cosine similarity)
- Linear scan over small FAQ dataset

### Cost
- Fully local inference
- No API cost at runtime
- One-time model download required

### Hallucination risk
- No generative model used
- Answers strictly retrieved from FAQ dataset
- Risk comes only from incorrect matching, not generation

---

## What would be improved with more time

- Add LLM-based reranking for uncertain matches
- Add simple UI (web or CLI improvements)
- Add weighted keyword boosting
- Add evaluation set to measure accuracy and fine tune thresholds
```
```