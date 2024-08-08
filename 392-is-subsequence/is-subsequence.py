class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for each character in s, check the character in t. if we find one, return continue
        # if reach max limit in t, 

        if not s or not s and not t:
            return True 
        elif not t:
            return False

        i = 0
        j = 0

        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i >= len(s):
                    return True
            else:
                j += 1
            

        return False

    
