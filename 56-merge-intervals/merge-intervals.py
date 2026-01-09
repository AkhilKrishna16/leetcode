class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the starting time 
        # 

        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]

        for i in range(1, len(intervals)):
            if ret[-1][1] >= intervals[i][0]:
                ret[-1][1] = max(intervals[i][1], ret[-1][1])
            else:
                ret.append(intervals[i])
        
        return ret