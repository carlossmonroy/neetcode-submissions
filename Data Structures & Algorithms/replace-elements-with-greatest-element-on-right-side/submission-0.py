class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                maximum=max(maximum,arr[j])
            arr[i]=maximum
            maximum=0
        arr[i]=-1
        return arr
