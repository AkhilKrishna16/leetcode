class Solution:
    def repeatedCharacter(self, s: str) -> str:
        h = set()

        for c in s:
            if c in h:
                return c
            h.add(c)
        return " "