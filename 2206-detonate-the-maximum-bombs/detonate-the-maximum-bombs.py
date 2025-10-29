class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def within_distance(anchor, distance):
            return anchor[2] >= (abs(distance[0] - anchor[0]) ** 2 + abs(distance[1] - anchor[1]) ** 2) ** (1/2)
        
        def dfs(circle, seen_on_path):
            count = 1
            for j in range(len(bombs)):
                if j not in seen_on_path and within_distance(circle, bombs[j]):
                    seen_on_path.add(j)
                    count += dfs(bombs[j], seen_on_path)
            return count
        ret = 0
        for i in range(len(bombs)):
            ret = max(dfs(bombs[i], {i}), ret)
        return ret