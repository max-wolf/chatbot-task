from faqs import load_faqs
from embeddings import EmbeddingModel
from matcher import SemanticMatcher
from chatbot import Chatbot


def main():
    print("Riverside Books chatbot")
    print("Type 'exit' to quit")

    faqs = load_faqs("faqs.json")
    embedder = EmbeddingModel()
    matcher = SemanticMatcher(faqs, embedder)
    bot = Chatbot(matcher)

    while True:
        query = input("> ")

        if query.lower() in ["exit"]:
            break

        result = bot.ask(query)
        print(result["answer"])


if __name__ == "__main__":
    main()