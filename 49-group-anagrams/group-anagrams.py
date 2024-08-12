class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string and check if strings are equal to each other 
        # ate, eat, tea -> [aet, aet, aet], [tan, tan], [abt]

        # create a hashmap for each string

        res = defaultdict(list)

        for string in strs:
             count = [0] * 26 # create hash_map psuedo

             for char in string:
                count[ord(char) - ord('a')] += 1 # add occurances
            
             res[tuple(count)].append(string) # add the count if it exists or add existing string if it maps
        
        return res.values()
             