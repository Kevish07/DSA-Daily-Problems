class Solution:
    #Function to find the largest number after k swaps.
    def findMaximumNum(self, s, k):
        #code here
        self.ans = s  # Start with original number as best

        def solve(idx, s, k):
            if k == 0 or idx >= len(s):
                if s > self.ans:
                    self.ans = s
                return

            max_char = max(s[idx:])  # Get max digit from current position to end

            if max_char != s[idx]:  # Only swap if there’s a better digit
                for j in range(len(s) - 1, idx, -1):
                    if s[j] == max_char:
                        s_list = list(s)
                        s_list[idx], s_list[j] = s_list[j], s_list[idx]
                        solve(idx + 1, ''.join(s_list), k - 1)
            else:
                solve(idx + 1, s, k)

        solve(0, s, k)
        return self.ans