class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pre = [pref[0]]
        for i in range(1, len(pref)):
            pre.append(pref[i] ^ pref[i - 1])
        return pre