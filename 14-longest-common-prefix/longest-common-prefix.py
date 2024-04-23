class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # iterate through the entire list repeatedly until one fails -> brute force
        # keep track of the longest prefix based on adjacent words
        # whenever they stop, move on to the next pair and see if it is lower, the only case we need to switch it

        longest_prefix = strs[0]
        current_prefix = strs[0]
        
        for i in range(1, len(strs)):
           
            current_prefix = ""
            for j in range(min(len(strs[i]), len(longest_prefix))):
                if strs[i][j] == longest_prefix[j]:
                    current_prefix += strs[i][j]
                else:
                    break
            
            if(len(current_prefix) < len(longest_prefix)):
                longest_prefix = current_prefix

        return longest_prefix