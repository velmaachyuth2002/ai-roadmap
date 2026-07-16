def remove_duplicates(nums: list[int]) -> int:
    fast=1
    slow=0
    while(fast<len(nums)):
        if nums[slow]==nums[fast]:
            fast+=1
        else:
            slow+=1
            nums[slow]=nums[fast]
            fast+=1
    return slow+1
nums=[1,1,2,2,3]
n=remove_duplicates(nums)
print(nums[:n])