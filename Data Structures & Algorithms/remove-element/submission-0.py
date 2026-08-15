class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slots = 0
        for i in range(len(nums)):
            if nums[i] == val:
                slots+=1
            else:
                nums[i-slots] = nums[i]
        return (len(nums)-slots)
