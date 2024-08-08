class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # iterate through all strings and each individual character 
        # have a current substring and a longest substring

        longest_substring = strs[0]
        current_substring = strs[0]

        for i in range(1, len(strs)):
            current_substring = ""
            for j in range(min(len(strs[i]), len(longest_substring))):
                if longest_substring[j] == strs[i][j]:
                    current_substring += strs[i][j]
                else:
                    break
            
            if len(longest_substring) > len(current_substring):
                longest_substring = current_substring
            
        return longest_substring
        
        