from collections import defaultdict
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        sm = 0
        res = 0
        dc = defaultdict(int)
        dc[0] = -1
        
        for ind, num in enumerate(arr):
            sm += 1 if num >k else -1
            if sm > 0:
                res = max(res, ind+1)
            else:
                if sm not in dc:
                    dc[sm] = ind
                    
                if sm-1 in dc:
                    res = max(res, ind - dc[sm-1])

        return res