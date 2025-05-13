class Solution:
    def nCr(self, n, r):
        # code here
        if r > n:
            return 0
        def factorial(num):
            fact = 1
            for i in range(1,num+1):
                fact *= i
            
            return fact
        
        one = factorial(n)
        two = factorial(r)
        diff = factorial(n-r)
        
        def ans(n,r,diff):
            res = (n) / ((r)*(diff))
            return int(res)
            
        res = ans(one,two,diff)
        return res