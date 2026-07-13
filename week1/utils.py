import time
print("utils loaded")

def dedupe(nums: list[int]) -> list[int]:
    result = []
    for num in nums:
      
        if num not in result:
            result.append(num)
    return result
def doc_frequency(dataset: list[dict]) -> dict[str, int]:
    newdic={}
    for items in dataset:
        newset=set(items["tokens"])
        for i in newset:
            if i in newdic:
                newdic[i]+=1
            else:
                newdic[i]=1
    return newdic
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
        averages[student] =round(
        total_scores[student] / subject_counts[student], 2
    )
    return averages
def time_lookup(collection, target, iterations: int = 1000) -> float:
    start = time.perf_counter()

    for _ in range(iterations):
        if target in collection:
            pass

    end = time.perf_counter()
    return end - start
def add_item(item, items=None):
    if items is None:
        items=[]
    items.append(item)
    return items

if __name__ == "__main__":
    print("utils loaded")

    



