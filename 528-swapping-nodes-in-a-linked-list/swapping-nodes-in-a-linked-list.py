# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p1 = head

        for _ in range(k - 1):
            p1 = p1.next
        
        fast = p1
        p2 = head

        while fast.next:
            fast = fast.next
            p2 = p2.next
            print(p2.val)
        
        p1.val, p2.val = p2.val, p1.val
        return head