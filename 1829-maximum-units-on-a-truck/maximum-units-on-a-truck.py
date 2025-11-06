class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0
        for boxes, boxUnits in boxTypes:
            total += min(truckSize, boxes) * boxUnits
            
            truckSize -= min(truckSize, boxes)
            if truckSize == 0:
                break
        return total