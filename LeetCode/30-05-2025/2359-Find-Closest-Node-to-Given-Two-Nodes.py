class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        one, two, i, j, res = set(), set(), node1, node2, -1
        one.add(i)
        two.add(j)
        while not one.__contains__(j) and not two.__contains__(i):
            if edges[i]!=-1:
                i = edges[i]
            if edges[j]!=-1:
                j = edges[j]
            if (one.__contains__(i) and two.__contains__(j)) or (one.__contains__(i) and j==-1) or (i==-1 and two.__contains__(j)) or (i==-1 and j==-1):
                break
            one.add(i)
            two.add(j)
        if one.__contains__(j) and two.__contains__(i):
            res = min(i, j)
        elif one.__contains__(j):
            res = j
        elif two.__contains__(i):
            res = i
        return res