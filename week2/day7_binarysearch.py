def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if nums[mid] == target:
            print(f"Iterations: {iterations}")
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Iterations: {iterations}")
    return -1


print(binary_search([1, 3, 5, 7, 9, 11], 7))   # 3
print(binary_search([1, 3, 5, 7, 9, 11], 1))   # 0
print(binary_search([1, 3, 5, 7, 9, 11], 11))  # 5
print(binary_search([1, 3, 5, 7, 9, 11], 4))   # -1
print(binary_search([], 5))                    # -1
print(binary_search([5], 5))                   # 0


big = list(range(1_000_000))

index = binary_search(big, 999_999)
print(index)