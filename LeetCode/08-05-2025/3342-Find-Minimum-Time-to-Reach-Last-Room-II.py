# Normal
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        
        # dist[i][j][parity] = min time to reach (i,j) with move count % 2 = parity
        dist = [[[float('inf')] * 2 for _ in range(m)] for _ in range(n)]
        # Priority queue: (time, i, j, moves)
        pq = [(0, 0, 0, 0)]  # Start at (0,0) with time 0 and 0 moves
        dist[0][0][0] = 0
        
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            time, i, j, moves = heapq.heappop(pq)
            
            # Skip if we've found a better time for this state
            if time > dist[i][j][moves % 2]:
                continue
            
            # If we reached the target, return the time
            if i == n - 1 and j == m - 1:
                return time
            
            # Try all 4 directions
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # Check if within bounds
                if 0 <= ni < n and 0 <= nj < m:
                    # Next move count and cost
                    next_moves = moves + 1
                    move_cost = 1 if next_moves % 2 == 1 else 2
                    
                    # Time to arrive at (ni, nj)
                    next_time = max(time, moveTime[ni][nj]) + move_cost
                    
                    # Update if this is a better time
                    if next_time < dist[ni][nj][next_moves % 2]:
                        dist[ni][nj][next_moves % 2] = next_time
                        heapq.heappush(pq, (next_time, ni, nj, next_moves))
        
        # Should always be reachable, but return -1 if not
        return -1


# Optimized
class Solution:
    def minTimeToReach(self, arr: List[List[int]]) -> int:
        m,n=len(arr),len(arr[0])
        dp=[[math.inf for i in range(n)] for j in range(m)]

        he=[]
        heappush(he,(0,1,0,0))
        vis=set()
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]

        while he:
            t,cost,x,y=heappop(he)
            if x==m-1 and y==n-1:
                return t

            for xx,yy in dirs:
                i,j=x+xx,y+yy

                if 0<=i<m and 0<=j<n and (i,j,cost) not in vis:
                    newtime=max(t,arr[i][j])+cost
                    vis.add((i,j,cost))
                    newcost = 1 if cost==2 else 2
                    heappush(he, (newtime, newcost , i, j))
            
