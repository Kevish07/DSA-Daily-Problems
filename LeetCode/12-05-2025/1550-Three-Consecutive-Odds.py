class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for x, y, z in permutations(digits, 3): 
            if x != 0 and z & 1 == 0: 
                ans.add(100*x + 10*y + z) 
        return sorted(ans)
    

# Optimized

from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_frequency = Counter(digits)
        result = []

        for number in range(100, 1000):
            if number % 2 != 0:
                continue

            current_frequency = Counter(map(int, str(number)))
            
            can_form = all(current_frequency[d] <= digit_frequency[d] for d in current_frequency)
            
            if can_form:
                result.append(number)
        
        return result