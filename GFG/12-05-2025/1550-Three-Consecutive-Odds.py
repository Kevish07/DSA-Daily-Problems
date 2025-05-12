class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        sample = []
        ans = False
        for i in range(len(arr)):
            sample.append(arr[i])
            counter += 1
            odd_counter = 0
            loop = 0
            if counter == 3:
                for j in range(len(sample)):
                    if sample[j]%2 == 1:
                        odd_counter += 1

                    if odd_counter == 3:
                        return True

                    loop += 1
                    if loop == 3:
                        counter = 2
                        odd_counter = 0
                        loop = 0
                        sample.pop(0)
        return ans
    
# Optimized

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0

        for num in arr:
            if num % 2 != 0:
                counter += 1
                if counter >= 3:
                    return True
            else:
                counter = 0

        return False