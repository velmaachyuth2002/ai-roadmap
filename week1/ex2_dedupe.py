import random
import time


def dedupe_version1_no_set(nums):
   
    result = []
    for num in nums:
      
        if num not in result:
            result.append(num)
    return result

def dedupe_version2_with_set(nums):
   
    result = []
    seen = set() 
    
    for num in nums:
  
        if num not in seen:
            result.append(num)
            seen.add(num) 
    return result


test_empty = []
test_dupes = [7, 7, 7]
test_sample = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]


print(f"Empty:  {test_empty} -> {dedupe_version2_with_set(test_empty)}")
print(f"Dupes:  {test_dupes} -> {dedupe_version2_with_set(test_dupes)}")
print(f"Sample: {test_sample} -> {dedupe_version2_with_set(test_sample)}")



large_input = [random.randint(0, 10000) for _ in range(50000)]




start_v1 = time.perf_counter()
res_v1 = dedupe_version1_no_set(large_input)
end_v1 = time.perf_counter()
time_v1 = end_v1 - start_v1
print(f"Version 1 (no set): {time_v1:.6f} s")

# Measure Version 2 (List + Set)
start_v2 = time.perf_counter()
res_v2 = dedupe_version2_with_set(large_input)
end_v2 = time.perf_counter()
time_v2 = end_v2 - start_v2
print(f"Version 2 (set):    {time_v2:.6f} s")


assert res_v1 == res_v2, "Error: The outputs do not match!"


ratio = time_v1 / time_v2
print(f"\nFinding: Set version is ~{ratio:.2f}x faster.")
