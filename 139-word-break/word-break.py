class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # have dp[i] = whether or not there are words in wordDict that can form from i onwards
        # for instance, dp[4] ("code") = True (since there is "code" in the dictionary)

        # dp[i] = dp[i + len(word)] if word == s[i: i + len(word)] for word in wordDict
        # return dp[0]
        # base case: dp[len(s)] = True
        # dp = [True] * (len(s) + 1)

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and word == s[i: i + len(word)]:
                    dp[i] |= dp[i + len(word)]
        
        return dp[0]