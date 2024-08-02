class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        # III -> 3
        # LVIII -> 50 + 5 + 1 + 1 + 1
        # MCMXCIV -> 1000 - 100 + 1000 - 10 + 100 - 1 + 5

        hash_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        for i in range(len(s) - 1):
            if hash_map[s[i]] >= hash_map[s[i + 1]]:
                total += hash_map[s[i]]
            elif hash_map[s[i]] < hash_map[s[i + 1]]:
                total -= hash_map[s[i]]
        
        total += hash_map[s[len(s) - 1]]

        return total