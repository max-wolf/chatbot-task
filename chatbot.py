class Chatbot:
    def __init__(self, matcher):
        self.matcher = matcher

    def ask(self, query: str):
        faq, score = self.matcher.find_best_match(query)

        if score < self.matcher.threshold:
            return {
                "answer": "Sorry, I don't know that one — please ask a member of staff.",
                "matched": None,
                "score": score
            }

        return {
            "answer": faq.answer,
            "matched": faq.id,
            "score": score
        }