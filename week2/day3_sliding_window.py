def max_window_sum(nums: list[int], k: int) -> int:
    max_sum=0
    for i,num in enumerate(nums):
        if i<k:
            max_sum+=num
        else:
            continue
    j=1
    n=k
    while n<len(nums):
        sum=max_sum-nums[j]+nums[n]
        max_sum=max(sum,max_sum)
        j+=1
        n+=1
    return max_sum
nums1=[2,1,5,1,3,2]
print(max_window_sum(nums1,3))
nums2=[1,1,1,1]
print(max_window_sum(nums2,2))
nums3=[5]
print(max_window_sum(nums3,1))
