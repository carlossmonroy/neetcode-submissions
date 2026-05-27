from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    suma=0
    for element in nums:
        suma+=element
    return suma

def get_min(nums: List[int]) -> int:
    min_actual=nums[0]
    for element in nums:
        if element < min_actual:
            min_actual=element
    return min_actual

def get_max(nums: List[int]) -> int:
    max_actual=nums[0]
    for element in nums:
        if element > max_actual:
            max_actual=element
    return max_actual

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
