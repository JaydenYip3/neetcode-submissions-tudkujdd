"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        for i in range(len(intervals)):
            if i == 0:
                continue
            if intervals[i - 1].end > intervals[i].start:
                return False
        
        return True
