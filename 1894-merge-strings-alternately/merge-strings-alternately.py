class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # designate a pointer for each word
        # consecutively add words until one of the pointers is longer than its word
        # at the end, figure out which one is maxed out and add the rest of the other word if any

        w1 = 0
        w2 = 0
        s = ''

        while w1 < len(word1) and w2 < len(word2):
            s += word1[w1]
            s += word2[w2]
            w1 += 1
            w2 += 1
        
        if w1 >= len(word1) and w2 <= len(word2):
            s += word2[w2:]
        elif w1 <= len(word1) and w2 >= len(word2):
            s += word1[w1:]
        
        return s