class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        i = 0
        start_i, end_i = newInterval
        new_intervals = []

        while i < len(intervals):
            if start_i <= intervals[i][0]:
                # found where to insert, left side merging
                if i == 0:
                    new_intervals.append(newInterval[::])
                elif i >= 1 and new_intervals[i-1][1] >= start_i:
                    new_intervals[i-1][1] = max(new_intervals[i-1][1], end_i)
                elif i >= 1 and new_intervals[i-1][1] < start_i:
                    new_intervals.append(newInterval[::])
                
                j = i
                while j < len(intervals):
                    if intervals[j][0] <= new_intervals[-1][1]:
                        new_intervals[-1][1] = max(new_intervals[-1][1], intervals[j][1])
                    else:
                        new_intervals.append(intervals[j])
                    j += 1

                newInterval.clear()
                i = j-1

            else:
                new_intervals.append(intervals[i])
            i += 1


        if newInterval:
            if new_intervals[-1][1] >= start_i:
                new_intervals[-1][1] = max(new_intervals[-1][-1], end_i)
            else:
                new_intervals.append(newInterval)
        return new_intervals
        
        



            

