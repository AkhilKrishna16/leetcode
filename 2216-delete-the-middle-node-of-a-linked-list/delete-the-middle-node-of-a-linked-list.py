# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        slow = head
        fast = head
        # 1 -> 3 -> 4 -> 7 -> 1 -> 2 -> 6
        # 1 -> 2 -> 3 -> 4
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next = slow.next
        else:
            head = slow.next
        
        return head
