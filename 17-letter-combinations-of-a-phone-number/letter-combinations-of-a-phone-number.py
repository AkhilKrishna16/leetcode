class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def dfs(i, curr_string):
            if len(curr_string) >= len(digits):
                res.append(curr_string)
                return
            
            for j in range(len(number_to_letters[digits[i]])):
                new_string = curr_string + number_to_letters[digits[i]][j]
                dfs(i + 1, new_string)

            
        dfs(0, "")
        return res

                
