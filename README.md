# Riverside Books — AI Grad Task

Welcome! This is a short, self-contained task. We're **not** looking for perfection —
we want to see how you think about and build a small AI-powered feature.

**Aim to spend no more than 2 hours on this.**

## The task

Build a simple command-line chatbot for a fictional independent bookshop,
**Riverside Books**. The bot answers customer questions using the FAQ data
provided in `faqs.json` (an array of `{ id, question, answer }` objects).

Our team works mainly in **Node and TypeScript**, so we'd prefer you build it
in TypeScript if you're comfortable — but if you're stronger in another
language, use that; we'd rather see your best work.

### Build the chatbot

- Use the question-and-answer pairs in `faqs.json` as your data.
- Take a question typed by the user.
- Match it to the most relevant FAQ and return the answer.
- Handle the case where there's no good match — the bot shouldn't confidently
  return a wrong answer. A sensible fallback (e.g. *"Sorry, I don't know that
  one — please ask a member of staff."*) is fine.
- Let the user keep asking questions until they type `quit` or `exit`.

### The interesting bit: how you match

This is the heart of the task, and **how you approach it is up to you.** A user
won't phrase their question exactly like the FAQ — "when can I come in?" should
still find the opening-hours answer despite sharing no words with it. How you
handle that is what we're most interested in.

Some directions you might take (all valid — pick what you think is right):

- **Embeddings / semantic search** — embed the FAQs and the user's question
  and match on similarity. A good free local option is
  `Xenova/all-MiniLM-L6-v2` via Transformers.js (`@xenova/transformers`),
  which runs in Node with no API key.
- **An LLM** — use OpenAI to pick the best FAQ, or to decide there's no good
  match. We'll provide a temporary OpenAI API key for this.
- **Something simpler** — keyword overlap or fuzzy matching is a perfectly
  reasonable starting point, especially if you explain the tradeoffs.

We're genuinely interested in your judgment here, not a particular answer.

### Use Git properly

- Commit your work in **logical steps** with clear messages
  (not one giant commit at the end).
- Push to a Git repository (GitHub or GitLab) and send us the link.
- Include a short README explaining how to run the bot.

### Optional: add a front end (bonus)

This is **entirely optional** and not required — the command-line version is
all we ask for. If you finish early and want to show a bit more, you're welcome
to add a simple front end that lets a user type a question and see the answer.
We build our front ends with Next.js, React, Tailwind, and shadcn/ui, so that's
a natural choice — but anything simple is fine. Don't let it eat into the core task.

## What we're looking at

| Area        | What we want to see                                          |
|-------------|--------------------------------------------------------------|
| Approach    | A sensible matching strategy and a clear rationale for it    |
| Coding      | Clean, readable code that works                              |
| AI judgment | Handling poor/no matches, and awareness of cost/latency/accuracy tradeoffs |
| Git         | A tidy commit history with meaningful messages               |

## Tell us how you thought about it

In your README, briefly cover:

- What matching approach you chose and **why**.
- How you handle the "no good answer" case.
- The tradeoffs of your approach (e.g. accuracy, latency, cost, hallucination
  risk) and what you'd do differently with more time.

We care as much about your reasoning as the code itself.

## Notes

- We'll provide a temporary **OpenAI API key** if you want to use an LLM or
  OpenAI embeddings. Never commit the key — read it from an environment
  variable and add it to your `.gitignore`.
- We work mainly in Node and TypeScript, so that's our preference — but use
  whatever lets you do your best work, and tell us what you chose.
- For context, our wider stack includes Next.js, React, Tailwind and shadcn/ui
  on the front end, and OpenAI and Claude for generation. You won't need most of that for this task — it's just a flavour
  of what you'd be working with.
- If you make assumptions, jot them down in your README.

---

*Good luck — and have fun with it!*
