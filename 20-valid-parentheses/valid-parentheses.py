class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {'{': '}', '(': ')', '[': ']'}
        for c in s:
            if c in '{([':
                stack.append(c)
            else:
                if not stack or m[stack.pop()] != c:
                    return False
        return not stack