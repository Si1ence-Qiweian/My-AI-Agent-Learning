with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)

import re
words = re.findall(r"[a-z]+", text.lower())
print(words)

stop_words = {
    "the", "is", "a", "an",
    "and", "to", "of", "in",
    "for", "it", "we"
}

filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)

counts = {}
for word in filtered_words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

top20 = sorted(
    counts.items(),
    key= lambda item: (-item[1], item[0])
)[:20]
print(top20)

print("========== Word Frequency ==========")

print(f"Total words: {len(filtered_words)}")
print(f"Unique words: {len(counts)}")

print("\nTop 20:\n")

for word, count in top20:
    print(f"{word:<15} {count}")