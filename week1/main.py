from utils import (dedupe,
    doc_frequency,
    student_averages,
    time_lookup,
    add_item,
)
# Test dedupe
nums = [1, 2, 2, 3, 1, 4, 5, 4]
print("Dedupe:", dedupe(nums))

# Test doc_frequency
dataset = [
    {"text": "great film", "label": 1, "tokens": ["great", "film"]},
    {"text": "awful pacing", "label": 0, "tokens": ["awful", "pacing"]},
    {"text": "great great pacing", "label": 1, "tokens": ["great", "great", "pacing"]},
]

print("Document frequency:", doc_frequency(dataset))

# Test student_averages
scores = {
    ("aditya", "math"): 91,
    ("aditya", "physics"): 78,
    ("aditya", "chem"): 85,
    ("meera", "math"): 88,
    ("meera", "physics"): 94,
}

print("Student averages:", student_averages(scores))

# Test time_lookup
numbers = list(range(100000))
numbers_set = set(numbers)

list_time = time_lookup(numbers, 99999)
set_time = time_lookup(numbers_set, 99999)

print(f"List lookup: {list_time} seconds")
print(f"Set lookup: {set_time} seconds")
print(f"Set is {list_time / set_time}x faster")


print(f"list is: {add_item(1)}")
print(f"list is: {add_item(2)}")
