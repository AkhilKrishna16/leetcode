class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we can utilize backtracking or some kind of dfs
        # basically, start from the top
        # then add every word 
        memo = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]
            
            res = False
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    res |= dfs(i + len(word))
            
            memo[i] = res
            return memo[i]
        
        return dfs(0)