class Solution:

    def perform_operation(self, token1, token2, operand):
        if operand == '+':
            return token1 + token2
        elif operand == '*':
            return token1 * token2
        elif operand == '-':
            return token2 - token1
        else:
            if token2 / token1 < 0:
                return int(ceil(token2 / token1))
            else:
                return int(floor(token2 / token1))
    def evalRPN(self, tokens: List[str]) -> int:
        # whenever we come across an operator, we take the last two recent operands, which we can
        # store and then perform the operation on that 

        # we can store operands through a stack
        # for specific integer division, we can just do floor for 
        # the positive result, and ceil for negative result

        stack = []
        res = 0
        

        for token in tokens:
            if token in "+-*/":
                token1 = token2 = 0
                if len(stack) >= 2:
                    token1 = stack.pop()
                    token2 = stack.pop()
                op_res = self.perform_operation(token1, token2, token)
                stack.append(op_res)
            else:
                stack.append(int(token))
        
        return stack[-1]



