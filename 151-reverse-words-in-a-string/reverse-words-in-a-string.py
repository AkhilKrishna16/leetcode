class Solution:
    def reverseWords(self, s: str) -> str:
        s = " " + s
        first = -1
        ret = ""
        for i in range(len(s) - 1, -1, -1):
            # drop the first pointer where the character is first seen
            # then continue until we reach a space, where we drop the second pointer
            if s[i] != ' ':
                if first == -1:
                    first = i
            elif s[i] == ' ':
                if first != -1:
                    ret += s[i + 1:first + 1]
                    ret += " "
                    first = -1
        
        return ret.strip()
