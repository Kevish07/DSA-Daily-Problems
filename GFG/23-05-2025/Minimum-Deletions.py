class Solution:
    def minDeletions(self,s):
        # code here 
        n = len(s)

        # Create a DP table for storing lengths of longest palindromic subsequences
        dp = [[0] * n for _ in range(n)]
    
        # All substrings of length 1 are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1
    
        # Build the table
        for cl in range(2, n + 1):  # cl is the length of the substring
            for i in range(n - cl + 1):
                j = i + cl - 1
                if s[i] == s[j] and cl == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    
        # The length of the longest palindromic subsequence is in dp[0][n-1]
        return n - dp[0][n - 1]