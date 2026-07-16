import time

print("utils loaded")


# Time Complexity: O(n²)

def dedupe(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result


# Time Complexity: O(N), where N is the total number of tokens across all documents
# The outer loop runs once per document, and the inner loop runs once per unique token
# in that document. It is not O(n²) because the loops are not both over the same input size.

def doc_frequency(dataset: list[dict]) -> dict[str, int]:
    newdic = {}

    for items in dataset:
        newset = set(items["tokens"])

        for i in newset:
            if i in newdic:
                newdic[i] += 1
            else:
                newdic[i] = 1

    return newdic


# Time Complexity: O(n), where n is the number of score entries

def student_averages(scores: dict) -> dict[str, float]:
    total_scores = {}
    subject_counts = {}

    for (student, subject), score in scores.items():

        if student in total_scores:
            total_scores[student] += score
            subject_counts[student] += 1
        else:
            total_scores[student] = score
            subject_counts[student] = 1

    averages = {}

    for student in total_scores:
        averages[student] = round(
            total_scores[student] / subject_counts[student], 2
        )

    return averages


# Time Complexity:
#   O(k*n) if collection is a list (k = iterations, n = collection size)
#   O(k) if collection is a set because lookup is O(1)

def time_lookup(collection, target, iterations: int = 1000) -> float:
    start = time.perf_counter()

    for _ in range(iterations):
        if target in collection:
            pass

    end = time.perf_counter()
    return end - start


# Time Complexity: O(1)

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items