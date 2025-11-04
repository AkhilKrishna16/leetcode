class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        q = deque(sorted(people))
        ret = 0

        while q:
            el = q.popleft()
            while q and q[-1] + el > limit:
                q.pop()
                ret += 1 # pop off everything that surpasses the limit
            
            # add the pair if there is a pair (0 and -1)
            if q:
                q.pop()

            ret += 1 # add one regardless
        
        return ret
            
            
