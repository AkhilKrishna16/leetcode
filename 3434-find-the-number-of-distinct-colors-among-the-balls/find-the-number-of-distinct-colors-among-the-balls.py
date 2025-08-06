class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        b_map = defaultdict(int)
        c_map = defaultdict(int)

        for query in queries:
            ball_id = query[0]
            color_id = query[1]

            if ball_id in b_map:
                old_value = b_map[ball_id]
                c_map[old_value] -= 1
                if c_map[old_value] == 0:
                    del c_map[old_value]
            b_map[ball_id] = color_id
            c_map[color_id] += 1
            res.append(len(c_map))
        return res


