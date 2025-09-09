class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # have a left sum and a right sum
        # count the number of customers that come during the right side and the left side
        # if close at i, you incur a penalty of right + ((i + 1) - left)
        prefix = [0]
        for i in range(len(customers)):
            if customers[i] == 'Y':
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        # right represent the number of Ys on the right and same with left
        ret = 0
        m = float('inf')
        for i in range(len(prefix)):
            curr = (prefix[-1] - prefix[i]) + (i - prefix[i])
            if curr < m:
                ret = i
                m = curr
            
        return ret
            
        
            
            