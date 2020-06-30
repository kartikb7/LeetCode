class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        start = 0

        while True:
            merged = False
            for j in range(start + 1, len(intervals)):
                if intervals[start][0] <= intervals[j][0] and intervals[start][1] >= intervals[j][1]:
                    intervals = intervals[:j] + intervals[j + 1:]
                    merged = True
                    break
                elif intervals[start][0] >= intervals[j][0] and intervals[start][1] <= intervals[j][1]:
                    intervals[start] = intervals[j]
                    intervals = intervals[:j] + intervals[j + 1:]
                    merged = True
                    break
                elif intervals[start][0] <= intervals[j][0] and intervals[start][1] >= intervals[j][0]:
                    intervals[start][1] = intervals[j][1]
                    intervals = intervals[:j] + intervals[j + 1:]
                    merged = True
                    break
                elif intervals[start][0] <= intervals[j][1] and intervals[start][1] >= intervals[j][1]:
                    intervals[start][0] = intervals[j][0]
                    intervals = intervals[:j] + intervals[j + 1:]
                    merged = True
                    break
            if not merged:
                start += 1
            if start >= len(intervals):
                break

        return intervals

