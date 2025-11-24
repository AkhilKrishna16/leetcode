class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1. What should the function take and return? 

        Talking about top-down, we need the minimum cost to climb the stairs.
        Define `dp(state)` such that it returns the minimum cost to climb stairs
        for a given state. 

        The only state variable that is relevant is `i`, the index of what 
        stair. Therefore, `dp(i)` should return the minimum cost to climb up
        to the ith step. 

        2. A recurrence relation to transition between states

        In `fib`, it was fib[n] = fib[n - 1] + fib[n - 2]. Here, it should be
        that to go to the 100th step (for instance), we must take the min of 
        cost up to the 98th step + cost of the 98th step or same with 99th step. 
        More generally, dp(i) = min(dp(i - 1) + cost[i - 1], dp(i - 2) + 
        cost[i-2]).

        3. Base case

        In this case, we know the answer for this because it gives us it in 
        the problem. 'You can either start from the step with index 0, 
        or the step with index 1.' Therefore, the cost of getting to these steps
        is 0. 
        """
        memo = {}
        def dp(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))
            return memo[i]
        
        return dp(len(cost))