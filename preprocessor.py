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

    # Synonym groups
    SYNONYM_GROUPS = {
        "time": [
            "opening hours", "opening times", "open", "close", "closing time", "hours", "shut"
        ],
        "location": [
            "address", "located", "where", "find you", "store", "shop"
        ],
        "gift_wrapping": [
            "gift wrap", "wrap gifts", "gift packaging"
        ],
        "order": [
            "order book", "out of stock", "not in stock", "special order", "backorder"
        ],
        "second_hand": [
            "used books", "second hand", "pre-owned", "sell books", "buy books"
        ],
        "events": [
            "author readings", "book club", "events", "signings"
        ],
        "parking": [
            "parking", "car park", "park nearby", "parking lot"
        ],
        "loyalty": [
            "loyalty", "rewards", "stamp card", "points"
        ],
        "vouchers": [
            "gift voucher", "gift card", "store credit"
        ],
        "payment": [
            "cash", "card", "contactless", "payment methods"
        ],
        "website": [
            "website", "online", "buy books", "order online", "click and collect online"
        ],
        "click_collect": [
            "click and collect", "pickup", "collect order", "in store pickup"
        ],
        "returns": [
            "return", "refund", "money back", "exchange"
        ],
        "children": [
            "kids", "child", "children", "children books", "kids books"
        ],
        "recommend": [
            "recommend", "suggest", "book advice", "what should i read"
        ],
        "cafe": [
            "cafe", "coffee", "tea", "snacks", "drinks"
        ],
        "accessibility": [
            "wheelchair", "disabled access", "step free", "accessible"
        ],
        "digital": [
            "ebook", "ebooks", "audiobook", "audiobooks", "digital books"
        ],
        "reserve": [
            "reserve", "hold book", "save book", "put aside"
        ],
        "student": [
            "student", "discount", "student discount", "cheap books"
        ]
    }

    @classmethod
    def preprocess(cls, query: str, debug: bool = False) -> str:
        query = query.lower()

        for pattern, replacement in cls.NORMALISATIONS.items():
            query = re.sub(pattern, replacement, query)

        words = re.findall(r"\b\w+\b", query)

        base_words = [w for w in words if w not in cls.STOPWORDS]

        seen = set()
        cleaned_base = []
        for w in base_words:
            if w not in seen:
                cleaned_base.append(w)
                seen.add(w)

        appended = []
        appended_seen = set()

        for w in cleaned_base:
            for group in cls.SYNONYM_GROUPS.values():
                if w in group:
                    for syn in group:
                        if syn not in seen and syn not in appended_seen:
                            appended.append(syn)
                            appended_seen.add(syn)

        final_tokens = cleaned_base + appended
        cleaned = " ".join(final_tokens)

        if debug:
            print(f"[DEBUG] base: {cleaned_base}")
            print(f"[DEBUG] appended: {appended}")
            print(f"[DEBUG] final: {cleaned}")

        return cleaned