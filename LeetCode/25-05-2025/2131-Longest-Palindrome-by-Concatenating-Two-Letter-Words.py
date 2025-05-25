class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        # Step 1: Square all elements
        squared = [x * x for x in arr]
        
        # Step 2: Sort the squared array
        squared.sort()
        
        # Step 3: Fix one element (c^2), and use two pointers for a^2 + b^2 = c^2
        for i in range(n - 1, 1, -1):
            c_sq = squared[i]
            left = 0
            right = i - 1
            while left < right:
                if squared[left] + squared[right] == c_sq:
                    return True
                elif squared[left] + squared[right] < c_sq:
                    left += 1
                else:
                    right -= 1
        return False