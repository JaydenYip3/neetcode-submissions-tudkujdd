class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        result = []
        i = 0
        intervals.sort(key=lambda key: key[0])

        while i < len(intervals):
            i += 1
            start = i - 1
            max_val = intervals[start][1]
            while i < len(intervals) and intervals[i][0] <= max_val:
                max_val = max(intervals[i][1], max_val)
                i += 1
            result.append([intervals[start][0], max_val])
        
        return result


        