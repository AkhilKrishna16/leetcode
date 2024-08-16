class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # convert licensePlate to just alpha lower chars 
        # iterate each word in words and check if every char is within licensePlate characterized
        # if so, take the lowest word
        # else, continue

        licensePlate = licensePlate.lower()
        shortest_word = None
        m = {}
        check = False

        for c in licensePlate:
            if c.isalpha():
                if c in m:
                    m[c] += 1
                else:
                    m[c] = 1
        
        for word in words:
            copy = m.copy()
            check = True
            for c in word:
                if c in copy and copy[c] >= 1:
                    copy[c] -= 1
            for value in copy.values():
                if value > 0:
                    check = False
                    break

            
            
            if check and shortest_word is None or check and len(word) < len(shortest_word) :
                shortest_word = word
            

        return shortest_word