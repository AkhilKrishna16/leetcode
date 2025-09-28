class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for c in s:
            if c != '#':
                stack1.append(c)
            elif stack1 and c == '#':
                stack1.pop()
        
        for c in t:
            if c != '#':
                stack2.append(c)
            elif stack2 and c == '#':
                stack2.pop()
        
        return "".join(stack1) == "".join(stack2)