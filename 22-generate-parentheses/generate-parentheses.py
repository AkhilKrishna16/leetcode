class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr_string, num_opens):
            if len(curr_string) - num_opens > num_opens or num_opens > n:
                return 
            elif len(curr_string) == n * 2:
                res.append(curr_string)
                return
            
            
            
            add_open = curr_string + "("
            dfs(add_open, num_opens + 1)
            close_open = curr_string + ")"
            dfs(close_open, num_opens)
        
        dfs("", 0)
        return res

