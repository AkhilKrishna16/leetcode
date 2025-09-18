class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            m[sorted_word].append(word)

        return list(m.values())