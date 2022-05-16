def removeDuplicates(nums):
    new_nums=[]
    count =1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            count+=1
        else:
            new_nums.append(nums[i])
    new_nums.append(nums[-1])
    for i in range(count-1):
        new_nums.append(0)
    return new_nums

print(removeDuplicates([1,1,1,2,2,3,3,3,3]))