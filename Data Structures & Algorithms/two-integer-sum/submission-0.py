class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_Dict = {}

        for i,n in enumerate(nums):
            difference = target - n

            if difference in my_Dict:
                return [my_Dict[difference], i]
            my_Dict[n] = i


