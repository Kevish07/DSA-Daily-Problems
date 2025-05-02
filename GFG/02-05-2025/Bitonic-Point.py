class Solution:

    def findMaximum(self, arr):
        n = len(arr)

        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if arr[m+1] < arr[m] > arr[m-1]:
                return arr[m]
            elif arr[m+1] > arr[m] > arr[m-1]:
                l = m + 1
            else:
                r = m - 1

        return -1
    

#  AI

class Solution:

    def findMaximum(self, arr):
        # code here
        n = len(arr)

        if n == 1:  # Handle edge case where the array has only one element
            return arr[0]

        l = 0
        r = n - 1
        while l <= r:
            m = (l + r) // 2

            # Handle edge cases for boundaries
            if m > 0 and m < n - 1 and arr[m - 1] < arr[m] > arr[m + 1]:
                return arr[m]
            elif m < n - 1 and arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m - 1

        return -1  # Return -1 if no bitonic point is found (shouldn't happen for valid input)