class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        # your viewing angle is optimal starting at the leftmost point;

        same_position = 0 
        angles = []

        lx, ly = location

        for x, y in points:
            dx = x - lx
            dy = y - ly
            
            if dx == 0 and dy == 0:
                same_position += 1
                continue

            a = math.degrees(math.atan2(dy, dx))
            

            if a < 0:
                a += 360
            angles.append(a)
        
        angles.sort()

        angles = angles + [a + 360 for a in angles]

        max_view = 0
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            
            max_view = max(max_view, min(right - left + 1, len(points)))
        
        return max_view + same_position