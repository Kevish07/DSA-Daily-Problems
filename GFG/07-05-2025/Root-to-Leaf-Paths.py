from typing import Optional
from collections import deque

from typing import List

"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def solve(self, root, ans, path):
        if not root:
            return
        
        path.append(root.data)
        
        if root.left is None and root.right is None:
            ans.append(path.copy())  # Use copy to avoid reference issues
        else:
            self.solve(root.left, ans, path)
            self.solve(root.right, ans, path)
        
        path.pop()  # Always backtrack after exploring both sides
        
    def Paths(self, root):
        ans = []
        self.solve(root, ans, [])
        return ans