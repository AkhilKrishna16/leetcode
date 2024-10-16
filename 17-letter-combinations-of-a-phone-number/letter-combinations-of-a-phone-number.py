class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = []

        if not digits:
            return []

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def traverse(index, combination): # we traverse every letter in the given digits str. 
        # if we reach the end of the digits string, we append the current string 
        # based on the current one, we call traverse again but we add onto the combination the current string
        

            if index == len(digits): # base case
                m.append(combination)
                return
            
            for keyword in keyboard[digits[index]]: # recursive call
                traverse(index + 1, combination + keyword)
        
        traverse(0, "")
        return m