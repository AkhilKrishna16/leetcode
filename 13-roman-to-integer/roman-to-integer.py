class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0 

        hashmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        for i in range(len(s) - 1):
            if hashmap[s[i]] >= hashmap[s[i + 1]]:
                total += hashmap[s[i]]
            else:
                total -= hashmap[s[i]]

        total += hashmap[s[-1]]


        return total