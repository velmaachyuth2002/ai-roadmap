from collections import Counter
dataset = [
    {"text": "great film", "label": 1, "tokens": ["great", "film"]},
    {"text": "awful pacing", "label": 0, "tokens": ["awful", "pacing"]},
    {"text": "great great pacing", "label": 1, "tokens": ["great", "great", "pacing"]},
]
counts=Counter(
    token
    for doc in dataset
    for token in set(doc["tokens"])
)
sorted_counts = sorted(
    counts.items(),
    key=lambda kv: kv[1],
    reverse=True
)

print(sorted_counts)

