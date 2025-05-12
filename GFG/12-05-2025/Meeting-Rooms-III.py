#User function Template for python3
import heapq
class Solution:
    def mostBooked(self, n, meetings):
        #code here
        # Min-heap for occupied rooms as (endTime, room)
        occupied = []

        # Min-heap for available room numbers
        available = list(range(n))
        heapq.heapify(available)

        # Count of meetings per room
        cnt = [0] * n

        # Sort meetings by start time
        meetings.sort()

        for start, end in meetings:
            # Free up rooms that are done before current meeting starts
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            if available:
                # Assign available room
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
                cnt[room] += 1
            else:
                # Delay meeting to when the next room is free
                endTime, room = heapq.heappop(occupied)
                duration = end - start
                heapq.heappush(occupied, (endTime + duration, room))
                cnt[room] += 1

        # Find the room with the most meetings
        maxCnt = max(cnt)
        for i in range(n):
            if cnt[i] == maxCnt:
                return i