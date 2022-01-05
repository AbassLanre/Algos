def twoSum( nums, target):
    #  initial thought
    # for i in range(len(nums)):
    #     for j in range(1,len(nums)):
    #         if nums[i] + nums[j]== target and i != j :
    #             return [i,j]
            
    for i,value_i in enumerate(nums):
        for j,value_j in enumerate(nums):
            if value_i +value_j == target and  i!=j:
                return [i,j]
                
print(twoSum([2,7,11,15], 9))