class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        is_consecutive, max_count=0,0
        for num in nums:
            if num == 1:
                is_consecutive+=1
            else:
                is_consecutive=0
            max_count=max(max_count,is_consecutive)
        return max_count
            
        