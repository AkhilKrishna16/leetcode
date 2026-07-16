class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # all we have to is consider the difference between the first and last element

        for i in range(len(timePoints)):
            timePoints[i] = int(timePoints[i][:2]) * 60 + int(timePoints[i][3:5])
        
        timePoints.sort()

        minDiff = float('inf')
        for i in range(1, len(timePoints)):
            minDiff = min(abs(timePoints[i] - timePoints[i - 1]), minDiff)
        
        minDiff = min(minDiff, 1440 - abs(timePoints[0] - timePoints[-1]))
    
        return minDiff
        