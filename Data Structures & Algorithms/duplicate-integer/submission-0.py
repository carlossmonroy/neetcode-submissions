class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}

        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] +=1
                return True
        return False