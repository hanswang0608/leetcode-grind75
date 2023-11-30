class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        start = -1
        end = -1
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                continue
            elif intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[1]:
                return intervals
            elif (newInterval[0] <= intervals[i][1] and newInterval[1] >= intervals[i][1]) or (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][0]) or (newInterval[0] <= intervals[i][0] and newInterval[1] >= intervals[i][1]):
                if start == -1:
                    start = i
                end = i
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            elif i - 1 >= 0 and newInterval[1] < intervals[i][0] and newInterval[0] > intervals[i-1][1]:
                print('here')
                intervals.insert(i, newInterval)
                return intervals
        if start == -1:
            intervals.append(newInterval)
        else:
            intervals = intervals[:start] + intervals[end+1:]
            intervals.insert(start, newInterval)
        return intervals
