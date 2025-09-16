#!/usr/bin/env python3
import random
from pync import Notifier

# ----------------------------
# Full paths to files
# ----------------------------
vocab_file = "/Users/mboatella/Documents/e.numerique/trois/projects/FrenchWords/levocab.txt"
history_file = "/Users/mboatella/Documents/e.numerique/trois/projects/FrenchWords/history.txt"

# ----------------------------
# Load vocabulary
# ----------------------------
with open(vocab_file, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

# ----------------------------
# Load history
# ----------------------------
try:
    with open(history_file, "r", encoding="utf-8") as f:
        used_words = set(line.strip() for line in f if line.strip())
except FileNotFoundError:
    used_words = set()

# ----------------------------
# Filter available words
# ----------------------------
available_words = [w for w in words if w not in used_words]

# Reset history if fewer than 4 words remain
if len(available_words) < 4:
    available_words = words
    used_words = set()

# ----------------------------
# Pick 5 words randomly
# ----------------------------
daily_words = random.sample(available_words, 4)

# Update history
used_words.update(daily_words)
with open(history_file, "w", encoding="utf-8") as f:
    for w in used_words:
        f.write(w + "\n")

# ----------------------------
# Print words
# ----------------------------
print("Les mots du jour:")
for word in daily_words:
    print("-", word)

# ----------------------------
# Desktop notification
# ----------------------------
Notifier.notify("\n".join(daily_words), title="French Words of the Day")