class Solution:
    def minTime(self, root, target):
        # code here
        parent_map = {}
        target_node = [None]
    
        def dfs(node, parent=None):
            if not node:
                return
            if node.data == target:
                target_node[0] = node
            parent_map[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)
    
        dfs(root)
    
        # Step 2: BFS from the target node to simulate burning
        visited = set()
        queue = deque()
        queue.append(target_node[0])
        visited.add(target_node[0])
    
        time = -1  # Start at -1 because first level (target node) is second 0
    
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
    
                # Visit left child
                if curr.left and curr.left not in visited:
                    visited.add(curr.left)
                    queue.append(curr.left)
                # Visit right child
                if curr.right and curr.right not in visited:
                    visited.add(curr.right)
                    queue.append(curr.right)
                # Visit parent
                parent = parent_map.get(curr)
                if parent and parent not in visited:
                    visited.add(parent)
                    queue.append(parent)
            time += 1
    
        return time