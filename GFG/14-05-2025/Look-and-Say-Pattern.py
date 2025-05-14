class Solution:
    def countAndSay(self, n):
        # code here
        if n == 1:
            return "1"
    
        result = "1"
        for _ in range(n - 1):
            current = ""
            i = 0
            while i < len(result):
                count = 1
                # Count consecutive same digits
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1
                # Append count followed by digit
                current += str(count) + result[i]
                i += 1
            result = current
    
        return result