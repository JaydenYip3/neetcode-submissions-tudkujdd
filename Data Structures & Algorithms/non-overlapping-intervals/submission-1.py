class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: (item[0],item[1]))
        end1 = intervals[0][1]
        result = 0
 
        for start, end in intervals[1:]:
            if start >= end1:
                end1 = end
            else:
                end1= min(end, end1)
                result += 1
        return result

        
        