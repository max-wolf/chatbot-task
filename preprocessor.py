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

    @classmethod
    def preprocess(cls, query: str) -> str:
        query = query.lower()

        for pattern, replacement in cls.NORMALISATIONS.items():
            query = re.sub(pattern, replacement, query)

        # remove extra whitespace
        query = " ".join(query.split())

        print(f"Processed query: {query}")

        return query