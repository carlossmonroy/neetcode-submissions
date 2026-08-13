import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    new_heap=[]
    for i in range(len(heap)-1,-1,-1):
        heapq.heappush(new_heap,heap[i])
    heapq.heappush(heap,value)
    return heap[0]


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
