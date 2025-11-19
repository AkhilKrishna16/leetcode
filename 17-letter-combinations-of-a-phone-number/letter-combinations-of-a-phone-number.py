class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret = []
        ln = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def dfs(i, curr_path):
            if i == len(digits):
                ret.append(curr_path)
                return
            
            for letter in ln[int(digits[i])]:
                dfs(i + 1, curr_path + letter)
            
        dfs(0, "")
        return ret
