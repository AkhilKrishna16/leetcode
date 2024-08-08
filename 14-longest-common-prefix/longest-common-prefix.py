class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # iterate through all strings and each individual character 
        # 
        
        longest_prefix = strs[0]
        current_prefix = strs[0]

        for i in range(1, len(strs)):
            current_prefix = ""
            for j in range(min(len(strs[i]), len(longest_prefix))):
                if strs[i][j] == longest_prefix[j]:
                    current_prefix += strs[i][j]
                else:
                    break
            
            if len(longest_prefix) > len(current_prefix):
                longest_prefix = current_prefix
        
        return longest_prefix