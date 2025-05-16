import heapq

class Solution:
    def findSmallestRange(self, arr):
        # code here
        k = len(arr)
        n = len(arr[0])
        
        min_heap = []
        max_value = float('-inf')
    
        for i in range(k):
            val = arr[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            max_value = max(max_value, val)
    
        # Initialize the result range with a large range
        range_start, range_end = -10**5, 10**5
    
        while True:
            min_value, row, idx = heapq.heappop(min_heap)
    
            # Update range if the current is smaller
            if max_value - min_value < range_end - range_start:
                range_start, range_end = min_value, max_value
    
            # If the current list is exhausted, stop
            if idx + 1 == len(arr[row]):
                break
    
            # Push next element from the same list
            next_val = arr[row][idx + 1]
            heapq.heappush(min_heap, (next_val, row, idx + 1))
            max_value = max(max_value, next_val)
    
        return [range_start, range_end]
            