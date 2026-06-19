import re


class QueryPreprocessor:
    NORMALISATIONS = {
        r"\bu\b": "you",
        r"\bur\b": "your",
        r"\bpls\b": "please",
        r"\bplz\b": "please",
        r"\bthx\b": "thanks",
        r"\binfo\b": "information",
        r"\br\b": "are",
        r"\by\b": "why"
    }

    STOPWORDS = {
        "a", "an", "the",
        "and", "or", "but",
        "do", "does", "did",
        "is", "was", "were",
        "can", "could", "would",
        "i", "we", "they",
        "to", "of", "in", "on", "for", "with",
        "my", "our", "you"
    }

    @classmethod
    def preprocess(cls, query: str, debug: bool = True) -> str:
        query = query.lower()

        # normalisation
        for pattern, replacement in cls.NORMALISATIONS.items():
            query = re.sub(pattern, replacement, query)

        # tokenisation + stopword removal
        words = re.findall(r"\b\w+\b", query)

        filtered = [
            w for w in words
            if w not in cls.STOPWORDS
        ]

        cleaned = " ".join(filtered)

        if debug:
            print(f"[DEBUG] cleaned query: {cleaned}")

        return cleaned