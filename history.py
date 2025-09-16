import os
import random

script_dir = os.path.dirname(os.path.realpath(__file__))
vocab_file = os.path.join(script_dir, "levocab.txt")
history_file = os.path.join(script_dir, "history.txt")

# Load all words
with open(vocab_file, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

# Load history if exists
if os.path.exists(history_file):
    with open(history_file, "r", encoding="utf-8") as f:
        used = set(line.strip() for line in f if line.strip())
else:
    used = set()

# Filter out already used words
available_words = [w for w in words if w not in used]

if not available_words:
    # Reset history if all words used
    available_words = words
    used = set()

# Pick one word
today_word = random.choice(available_words)
print(f"Word of the day: {today_word}")

# Add to history
used.add(today_word)
with open(history_file, "w", encoding="utf-8") as f:
    for w in used:
        f.write(w + "\n")