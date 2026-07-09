"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: (interval.start, interval.end))

        rooms = [] 
        for interval in intervals:
            start = interval.start
            end = interval.end
            exit_status = True
            for i in range(len(rooms)):
                if start >= rooms[i][1]:
                    rooms[i] = (start, end)
                    exit_status = False
                    break
            if exit_status:
                rooms.append((start,end))

        
        return len(rooms)
        
            




        