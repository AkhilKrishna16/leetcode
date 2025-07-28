class Solution:
    def isHappy(self, n: int) -> bool:
        def generate_next_value(n: int) -> int:
            copy = n
            s = 0
            while copy > 0:
                s += (copy % 10) ** 2
                copy //= 10
            
            return s
        
        slow = generate_next_value(n)
        fast = generate_next_value(generate_next_value(n))

        while slow != fast:
            if slow == fast:
                break
            slow = generate_next_value(slow)
            fast = generate_next_value(generate_next_value(fast))
        return slow == 1