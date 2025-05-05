# TLE [Time limit exceed]
class Solution:
    def numTilings(self, n: int) -> int:
        mod = int(1e9 + 7)
        
        def dominoes(i, n, possible):
            if i == n:
                return 0 if possible else 1
            if i > n:
                return 0
            if possible:
                return (dominoes(i + 1, n, False) + dominoes(i + 1, n, True)) % mod
            return (dominoes(i + 1, n, False) + dominoes(i + 2, n, False) + 2 * dominoes(i + 2, n, True)) % mod
        
        return dominoes(0, n, False)
    
# Optimized
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        arr = [0] * max(3, n)
        arr[0] = 1  # n = 1
        arr[1] = 2  # n = 2
        arr[2] = 5  # n = 3
        for i in range(3, n):
            arr[i] = (2 * arr[i - 1] + arr[i - 3]) % MOD
        return arr[n - 1]