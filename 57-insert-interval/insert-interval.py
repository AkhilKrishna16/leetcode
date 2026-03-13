class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # what are the different cases?
        # the new interval should be added to end
        # the new interval should be inserted in the middle
        # the new interval should be insert at the start

        # first, you want to find where the starting point should be
        # this involves finding where startIndex, which is where the newInterval_start is <= the start of the next
        # 
        # then after that you want to merge the intervals,
        # this involves going back as far as you can and finding where end < start_new
        # then you must merge in front
        # this involves going as far in front until start_i > end_new

        ret = []

        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1
            
        print(i)
        # we have added all the intervals that don't need to be merged

        start = newInterval[0]
        end = newInterval[1]
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            # merge everything
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        
        ret.append([start, end])

        while i < len(intervals):
            ret.append(intervals[i])
            i += 1

        return ret