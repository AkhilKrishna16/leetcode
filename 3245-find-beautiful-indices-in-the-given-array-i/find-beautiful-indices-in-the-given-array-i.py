class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # iterate with starting from the beginning for the iteration of `s`
        # at a pace of `len(a)` characters until `len(s) - len(a) + 1`
        # then, for each of those, essentially iterate `k` out for both sides 
        # whenever the next `len(a)` characters starting from `i` match `a`
        # for that iteration, it should just be trying to match the characters for `b`
        ret = []
        a_indices = []
        for i in range(len(s) - len(a) + 1):
            if s[i:i + len(a)] == a:
                a_indices.append(i)
        
        b_indices = []
        for i in range(len(s) - len(b) + 1):
            if s[i: i + len(b)] == b:
                b_indices.append(i)
        
        # find where points are within k distance of one another
        print(a_indices, b_indices)
        for i in a_indices:
            for j in b_indices:
                if abs(i - j) <= k:
                    ret.append(i)
                    break
        return ret
                
