class Solution:
    def longestPalindrome(self, s: str) -> int:
        # check if we have an even parity of a specific character
        # we can measure even parity by scanning the string and adding corresponding to a hashmap
        # a: 1, b: 1, c: 4, d: 2
        # 6 + 1 if one is a length of one than we must exclude it 
        # abcdd
        # a: 1, b: 1, c: 1, d: 2 add two d's and one of the other characters 
        # have a marker to mark if we have encounter a one occurance string

        # abbcccccddd
        # a: 1, b: 2, c: 1, d: 3 -> we can only have one odd parity character in the string 
        # if the character is more than that, we must get rid of it 
        # track the greatest_odd_parity, we can add that to get the most letters
        # once we add that one, every other one can just be added as m[c_k] - 1

        m = {}

        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        
        total_str = 0
        odd_found = False
        
        for c_k in m:
            if m[c_k] % 2 == 0:
                total_str += m[c_k]
            else:
                total_str += m[c_k] - 1
                odd_found = True
        
        if odd_found:
            total_str += 1
        return total_str
            
                