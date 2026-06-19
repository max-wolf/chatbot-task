class Chatbot:
    def __init__(self, matcher, debug=True):
        self.matcher = matcher
        self.debug = debug

    def ask(self, query: str):
        matches = self.matcher.find_matches(query, k=3)

        if not matches:
            return {
                "answer": "Sorry, I don't know that one — please ask a member of staff.",
                "score": 0.0
            }

        # unpack best result
        best_faq, best_score = matches[0]

        # DEBUG OUTPUT
        if self.debug:
            print("\n[DEBUG] Top matches:")
            for faq, score in matches:
                print(f"{score:.3f} -> {faq.question}")

            print(f"[DEBUG] Selected: {best_faq.question} ({best_score:.3f})\n")

        # threshold decision
        if best_score < self.matcher.threshold:
            return {
                "answer": "Sorry, I don't know that one — please ask a member of staff.",
                "score": best_score
            }

        return {
            "answer": best_faq.answer,
            "score": best_score
        }