class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        mark = 0

        for i in range(len(str1)):
            res = ord(str1[i]) - ord(str2[mark])

            if res == 0 or res == -1 or res == 25:
                mark += 1

            if mark == len(str2):
                break

        
        return mark == len(str2)
