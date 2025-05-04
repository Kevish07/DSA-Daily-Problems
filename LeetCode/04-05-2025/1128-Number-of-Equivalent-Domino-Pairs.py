# TLE [Time limit exceed]
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        count = 0
        for i in range(len(dominoes)):
            for j in range(i + 1, n):
                a, b = dominoes[i]
                c, d = dominoes[j]
                if (a == c and b == d) or (a == d and b == c):
                    count += 1
        return count
    
# Optimized
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        mpp = [0] * 100
        count = 0
        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            count += mpp[key]
            mpp[key] += 1
        return count