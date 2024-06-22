class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l = {}
        j = {}

        # Count characters in s
        for c in s:
            if c not in l:
                l[c] = 1
            else:
                l[c] += 1

        # Count characters in t
        for m in t:
            if m not in j:
                j[m] = 1
            else:
                j[m] += 1

        # Compare the two dictionaries
        return l == j
