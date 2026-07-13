scores = {
    ("aditya", "math"): 91,
    ("aditya", "physics"): 78,
    ("aditya", "chem"): 85,
    ("meera", "math"): 88,
    ("meera", "physics"): 94,
}

total_scores = {}
subject_counts = {}
for key, score in scores.items():
    student = key[0]

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

print(averages)