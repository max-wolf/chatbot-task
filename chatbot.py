class Chatbot:
    def __init__(self, matcher, debug=False, gap_threshold=0.05):
        self.matcher = matcher
        self.debug = debug
        self.gap_threshold = gap_threshold

    def ask(self, query: str):
        matches = self.matcher.find_matches(query, k=2)

        if not matches:
            return {
                "answer": "Sorry, I don't know that one — please ask a member of staff.",
                "score": 0.0
            }

        best_faq, best_score = matches[0]

        second_score = matches[1][1] if len(matches) > 1 else 0.0

        gap = best_score - second_score

        # DEBUG OUTPUT
        if self.debug:
            print("\n[DEBUG] Top matches:")
            for faq, score in matches:
                print(f"{score:.3f} -> {faq.question}")

            print(f"[DEBUG] Best score: {best_score:.3f}")
            print(f"[DEBUG] Second score: {second_score:.3f}")
            print(f"[DEBUG] Gap: {gap:.3f}\n")

        # threshold check
        if best_score < self.matcher.threshold:
            return {
                "answer": "Sorry, I don't know that one — please ask a member of staff.",
                "score": best_score
            }

        # ambiguity check
        if gap < self.gap_threshold:
            return {
                "answer": "Sorry, I'm not confident about that — please ask a member of staff.",
                "score": best_score
            }

        return {
            "answer": best_faq.answer,
            "score": best_score
        }