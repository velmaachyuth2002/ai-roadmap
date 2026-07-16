def twosum_unsorted(nums:list[int],target:int):
    dict1={}
    for i,num in enumerate(nums):
        rem=target-num
        if rem in dict1:
            return [i,dict1[rem]]
        else:
            dict1[num]=i
    return []
nums=[2,3,4]
list1=twosum_unsorted(nums,6)
print(list1)
