class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        q = deque(stones)

        while len(q) > 1:
            print(q)
            el1 = q.popleft()
            el2 = q.popleft()

            # append the difference between the two
            diff = abs(el1 - el2)
            # you cant just append you have to sort the queue again
            q.append(diff)
            q = deque(sorted(q, reverse=True))
        
        return q[0]