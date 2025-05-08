class Solution:
    def findMissing(self, arr):
        # code here
        n = len(arr) + 1  # total terms including the missing one
        d = (arr[-1] - arr[0]) // (n - 1)
        if (arr[1] - arr[0]) == (arr[2] - arr[1]):
            d = (arr[1] - arr[0])
        elif (arr[2] - arr[1]) == (arr[3] - arr[2]):
            d = (arr[2] - arr[1])
            
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != d:
                return arr[i] + d
        return arr[-1] + d  # No deviation found, return next element