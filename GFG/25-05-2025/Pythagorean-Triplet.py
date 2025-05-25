class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        squares = set()
        
        # Insert all squares into a set
        for num in arr:
            squares.add(num * num)
        
        # Check all pairs (a, b)
        for i in range(n):
            for j in range(i + 1, n):
                sum_sq = arr[i] * arr[i] + arr[j] * arr[j]
                if sum_sq in squares:
                    # Now make sure that the index of c is different
                    c = int(sum_sq ** 0.5)
                    # If c is perfect square and present in array
                    if c in arr:
                        # Ensure c is not at index i or j
                        for k in range(n):
                            if k != i and k != j and arr[k] == c:
                                return True
        return False