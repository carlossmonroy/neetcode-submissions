class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        is_consecutive, consecutive_list=0,[]
        for num in nums:
            if num == 1:
                is_consecutive+=1
            else:
                is_consecutive=0
            consecutive_list.append(is_consecutive)
        return max(consecutive_list)
            
        