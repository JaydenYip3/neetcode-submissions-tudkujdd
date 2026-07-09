"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda interval:(interval.start, interval.end))

        heap = []
        rooms = 0

        for interval in intervals:
            if heap and interval.start >= heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,interval.end)
            else:
                heapq.heappush(heap, interval.end)
            rooms = max(len(heap), rooms)
        
        return rooms

        
            




        