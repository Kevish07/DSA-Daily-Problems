class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        freq = [[0] * 26 for _ in range(n)]
        visited = [0] * n
        cycle = [0] * n
        
        def DFS(i):
            if cycle[i]:
                return float('inf')
            if visited[i]:
                return freq[i][ord(colors[i]) - ord('a')]
            visited[i] = cycle[i] = 1
            for j in adj[i]:
                if DFS(j) == float('inf'):
                    return float('inf')
                for x in range(26):
                    freq[i][x] = max(freq[i][x], freq[j][x])
            cycle[i] = 0
            freq[i][ord(colors[i]) - ord('a')] += 1
            return freq[i][ord(colors[i]) - ord('a')]
        ans = 0
        for u in range(n):
            val = DFS(u)
            if val == float('inf'):
                return -1
            ans = max(ans, val)
        return ans
