"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

"""

class Solution:
    def primeList(self, head):
        # code here

        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2,int(num**0.5)+1):
                if num%i == 0:
                    return False
            return True
        
        def nearest_prime(n):
            if is_prime(n):
                return n
                
            prev = n - 1
            next_ = n + 1
            while True:
                if prev >= 2 and is_prime(prev):
                    return prev
                if is_prime(next_):
                    return next_
                prev -= 1
                next_ += 1
        

        temp = head
        while temp:
            temp.val = nearest_prime(temp.val)
            temp = temp.next
        return head