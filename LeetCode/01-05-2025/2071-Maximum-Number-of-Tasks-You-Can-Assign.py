class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def can_finish(mid, pills):
            
            n = len(workers)
            i = 0
            queue = deque()
            
            for j in range(n - mid, n):
                w = workers[j]

                while i < mid and tasks[i] <= w + strength:
                    queue.append(tasks[i])
                    i += 1

                if not queue:
                    return False

                if queue[0] <= w:
                    queue.popleft()
                else:
                    if pills == 0:
                        return False
                    pills -= 1
                    queue.pop()
            return True
        
        left = 0
        right = min(len(tasks), len(workers))
        
        while left< right:
            
            mid = (left + right + 1 ) // 2
            if can_finish(mid, pills):
                left = mid
            else:
                right = mid - 1
        return left
    