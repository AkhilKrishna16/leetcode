class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_string_list = []

        def is_palindrome(text):
            start = 0
            end = len(text) - 1
            while start < end:
                if text[start] != text[end]:
                    return False
                start += 1
                end -= 1
            
            return True

        def dfs(i):
            if i == len(s):
                res.append(curr_string_list.copy())
                return
            for j in range(i, len(s)):
                substring = s[i:j + 1]
                if is_palindrome(substring):
                    curr_string_list.append(substring)
                    dfs(j + 1)
                    curr_string_list.pop()
        dfs(0)
        return res
            
