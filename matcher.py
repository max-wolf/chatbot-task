import numpy as np


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class SemanticMatcher:
    def __init__(self, faqs, embedder, threshold=0.7):
        self.faqs = faqs
        self.embedder = embedder
        self.threshold = threshold  # FIXED

        self._precompute_embeddings()

    def _precompute_embeddings(self):
        for faq in self.faqs:
            text = f"Question: {faq.question} Answer: {faq.answer}"
            faq.embedding = self.embedder.embed(text)

    def find_best_match(self, query: str):
        query_embedding = self.embedder.embed(query)

        best_faq = None
        best_score = -1

        for faq in self.faqs:
            score = cosine_similarity(query_embedding, faq.embedding)

            if score > best_score:
                best_score = score
                best_faq = faq

        if best_score < self.threshold:
            return None, best_score

        return best_faq, best_score