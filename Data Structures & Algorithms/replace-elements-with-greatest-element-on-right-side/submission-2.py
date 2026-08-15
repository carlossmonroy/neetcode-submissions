class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum_so_far = -1

        for i in range (len(arr) -1, -1, -1):
            if arr[i] > maximum_so_far:
                arr[i], maximum_so_far = maximum_so_far, arr[i]
            else:
                arr[i] = maximum_so_far

        return arr
