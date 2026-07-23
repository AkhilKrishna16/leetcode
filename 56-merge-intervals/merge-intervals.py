class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            print(intervals[i])
            if merged[-1][1] >= intervals[i][0]:
                print("here")
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
                
            else:
                merged.append(intervals[i])
        
        return merged
