class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if not tops or not bottoms or not len(tops) == len(bottoms):
            return -1

        top = self.checkRotations(tops, bottoms, tops[0])
        if top != -1:
            return top
        else:
            return self.checkRotations(tops, bottoms, bottoms[0])

    def checkRotations(self, tops, bottoms, target):
        topRotation = 0
        bottomRotation = 0

        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1

            if tops[i] != target:
                topRotation += 1

            if bottoms[i] != target:
                bottomRotation += 1
 
        return min(topRotation, bottomRotation)




# Optimized
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        res = check(tops[0])
        if res != -1:
            return res
        return check(bottoms[0])