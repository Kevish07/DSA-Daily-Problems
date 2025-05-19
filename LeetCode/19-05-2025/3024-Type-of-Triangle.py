class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        var1 = nums[0]
        var2 = nums[1]
        var3 = nums[2]
        if var1 + var2 > var3:
            if var1 == var2 == var3:
                return "equilateral"
            elif var1 == var2 or var1 == var3 or var2 == var3:
                return "isosceles"      
            else:
                return "scalene"
        else:
            return "none"