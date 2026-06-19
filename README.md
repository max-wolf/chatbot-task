# Semantic Search Chatbot

How it works:
User enters a question
Query is preprocessed:
lowercase normalisation
slang expansion (u → you, pls → please)
stopword removal
deduplication
synonym group expansion (append-only)
Query is embedded
Compared against precomputed FAQ embeddings
Top 2 matches retrieved
Decision made using:
similarity threshold
score gap

Running:
Create virtual environment
Install dependencies from requirements.txt
Normal mode:
python main.py
Debug mode:
python main.py --debug


add some simple regex -> "u" convert to "you"
add LLM and combine with semantic for improved estimation
add UI
further testing: ID 15 fails with remove of capitalisation
more case handling