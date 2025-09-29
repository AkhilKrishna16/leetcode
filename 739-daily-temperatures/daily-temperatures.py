class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                answer = i - popped
                ret[popped] = answer
            stack.append(i)
        
        return ret