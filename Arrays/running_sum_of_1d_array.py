def runningSum(self, nums: List[int]) -> List[int]:
    count =0
    ans=[]
    for i in range(len(nums)):
        count+=nums[i] 
        ans.append(count)
        
    return ans