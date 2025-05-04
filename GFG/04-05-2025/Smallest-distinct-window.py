class Solution:
    def findSubString(self, str):
        # code here
        s = str
        n = len(s)
        if n == 0:
            return 0
    
        unique_chars = set(s)
        required = len(unique_chars)
        
        freq_map = {}
        formed = 0
        left = 0
        min_len = float('inf')
        
        for right in range(n):
            char = s[right]
            # Update frequency count manually
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
    
            # Count unique characters added to window
            if freq_map[char] == 1:
                formed += 1
    
            # Try to minimize window size
            while formed == required:
                min_len = min(min_len, right - left + 1)
    
                # Remove or decrement frequency of left char
                left_char = s[left]
                freq_map[left_char] -= 1
                if freq_map[left_char] == 0:
                    formed -= 1
                left += 1
    
        return min_len