class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        result = []
        i = 0
        intervals.sort(key=lambda key: key[0])

        while i < len(intervals):
            start = i
            max_val = intervals[i][1]
            while i + 1 < len(intervals) and intervals[i + 1][0] <= max_val:
                i += 1
                max_val = max(intervals[i][1], max_val)
            result.append([intervals[start][0], max_val])
            i += 1
        
        return result


        