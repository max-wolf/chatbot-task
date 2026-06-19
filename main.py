import argparse

from chatbot import Chatbot
from matcher import SemanticMatcher
from embeddings import EmbeddingModel
from faqs import load_faqs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    faqs = load_faqs("faqs.json")

    embedder = EmbeddingModel()
    matcher = SemanticMatcher(faqs, embedder, threshold=0.6)

    bot = Chatbot(matcher, debug=args.debug)

    print("Riverside Books chatbot")
    print("Type 'exit' to quit")

    while True:
        query = input("> ")

        if query.lower() in ["exit", "quit"]:
            break

        result = bot.ask(query)
        print(result["answer"])


if __name__ == "__main__":
    main()