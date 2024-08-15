class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = {}
        l = []
        mi = float('inf')

        for i, l1 in enumerate(list1):
            for j, l2 in enumerate(list2):
                if l1 == l2:
                    if l1 in m:
                        m[l1] = min(m[l1], i + j)
                    else:
                        m[l1] = i + j

        for k in m.keys():
            if m[k] < mi:
                l.clear()
                l.append(k)
                mi = m[k]
            elif m[k] == mi:
                l.append(k)
        
        return l
            
        
        return 

