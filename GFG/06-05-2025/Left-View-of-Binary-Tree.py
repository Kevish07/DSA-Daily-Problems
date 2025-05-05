class Solution:
    def LeftView(self, root):
        # code here
        if root is None or root == "N":
            return []
    
        q = []
        lst = []
        q.append(root)
    
        while q:
            level_size = len(q)
            for i in range(level_size):
                pop = q.pop(0)
                if pop is None:
                    continue  # Skip None nodes
    
                if i == 0:  # First node at this level
                    lst.append(pop.data)
    
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
        
        return lst