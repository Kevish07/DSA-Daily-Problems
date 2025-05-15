from collections import Counter
class Solution:
    def countSubstring(self, s):
        freq = Counter(s)
        total = 0
        for f in freq.values():
            total += (f * (f + 1)) // 2
        return total