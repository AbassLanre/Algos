def removeDuplicates(nums):
    # new_nums=[]
    # count =1
    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         count+=1
    #     else:
    #         new_nums.append(nums[i])
    # new_nums.append(nums[-1])
    # for i in range(count-1):
    #     new_nums.append(0)
    count = 0

    for i in nums:
        while nums.count(i) > 1:
            nums.pop(nums.index(i))
            count = count + nums.count(i)
    for g in range(count-1):
        nums.append('_')
    return nums,len(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))