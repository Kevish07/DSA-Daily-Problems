class Solution:
    def findTarget(self, arr, target):
        # code here
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1