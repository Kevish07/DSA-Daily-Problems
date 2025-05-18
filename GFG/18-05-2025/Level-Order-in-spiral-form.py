from collections import deque
class Solution:
    def findSpiral(self, root):
        #code here
        if not root:
            return []
    
        result = []
        queue = deque([root])
        level = 0
    
        while queue:
            level_size = len(queue)
            current_level = []
    
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.data)
    
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
            # Reverse current level if even level (0-based index)
            if level % 2 == 0:
                result.extend(current_level[::-1])
            else:
                result.extend(current_level)
    
            level += 1
    
        return result