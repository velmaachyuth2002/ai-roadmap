def two_sum_sorted(nums:list[int],target:int) -> list[int]:
    i=0
    j=len(nums)-1

    while(i<j):
        sum=nums[i]+nums[j]
        if(sum==target):
            return [i,j]
        elif(sum>target):
            j-=1
        else:
            i+=1
    return "target not found"
print(two_sum_sorted([2, 7, 11, 15], 9 ))
print(two_sum_sorted([1, 2, 3, 4, 6], 6 ))
print(two_sum_sorted([5, 25, 75], 100  ))
