import numpy as np
from preprocessor import QueryPreprocessor


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class SemanticMatcher:
    def __init__(self, faqs, embedder, threshold=0.45):
        self.faqs = faqs
        self.embedder = embedder
        self.threshold = threshold  # FIXED

        self._precompute_embeddings()

    def _precompute_embeddings(self):
        for faq in self.faqs:
            text = f"Question: {faq.question} Answer: {faq.answer}"
            faq.embedding = self.embedder.embed(text)

    def find_matches(self, query: str, k=3):
        query = QueryPreprocessor.preprocess(query)

        query_embedding = self.embedder.embed(query)

        results = []

        for faq in self.faqs:
            score = cosine_similarity(
                query_embedding,
                faq.embedding
            )

            results.append((faq, score))

        results.sort(
            key=lambda x: x[1],
            reverse=True
        )

        return results[:k]