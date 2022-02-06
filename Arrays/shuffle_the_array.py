    def shuffle(self, nums: List[int], n: int) -> List[int]:
        listA = nums[0:n]
        listB = nums[n:]
        newNums=[]
        for i in range(n):
            newNums.append(listA[i])
            newNums.append(listB[i])

        return newNums