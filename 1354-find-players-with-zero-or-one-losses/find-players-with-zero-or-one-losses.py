class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        m = defaultdict(int)

        for match in matches:
            m[match[1]] += 1
            m[match[0]] += 0
        
        ret = [[], []]

        for key in m:
            if m[key] == 0:
                ret[0].append(key)
            elif m[key] == 1:
                ret[1].append(key)
        ret[0] = sorted(ret[0])
        ret[1] = sorted(ret[1])
        
        return ret