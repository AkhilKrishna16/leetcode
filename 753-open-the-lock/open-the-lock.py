class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def compute_next_locks(lock):
            new_locks = []
            for i in range(len(lock)):
                # this can wrap around so mod it by 10
                # you also have to account for the minuses
                plus_lock = lock[:i]
                minus_lock = lock[:i]
                plus_lock += f"{(int(lock[i]) + 1) % 10}"
                plus_lock += lock[i + 1:]
                minus_lock += f"{(int(lock[i]) - 1) % 10}"
                minus_lock += lock[i + 1:]
                new_locks.append(plus_lock)
                new_locks.append(minus_lock)
            return new_locks
        
        q = deque([("0000", 0)])
        seen = {"0000"}

        # while the q has elements 
        # iterate through every element at the current level 
        
        while q:
            curr_lock, steps = q.popleft()
            if curr_lock == target:
                return steps
            
            next_locks = compute_next_locks(curr_lock)
            for next_lock in next_locks: # for every neighbor
                if next_lock not in deadends and next_lock not in seen:
                    seen.add(next_lock)
                    q.append((next_lock, steps + 1))
        
        return -1
