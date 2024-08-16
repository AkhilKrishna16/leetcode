class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # convert each to the appropriate morse code values
        # check if morse code values are equal to each other
        # and count the number of unique morse codes
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()

        for word in words:
            new_word = ""
            for i in range(len(word)):
                ch = morse_code[ord(word[i]) - 97]
                new_word += ch

            s.add(new_word)

        
        return len(s)