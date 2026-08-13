import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap,list_of_values=[],[]
    for num in nums:
        pair=(-(num),num)
        heapq.heappush(heap,pair)
    
    while heap:
        pair=heapq.heappop(heap)
        list_of_values.append(pair[1])
    return list_of_values



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
