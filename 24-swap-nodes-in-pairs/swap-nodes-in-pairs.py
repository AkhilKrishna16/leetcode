# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr, curr.next
        # next_node = head.next.next
        # head.next.next = head
        # if not prev: prev = head
        # prev.next = head.next
        # head.next = next_node

        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr and curr.next:
            next_node = curr.next.next
            curr.next.next = curr
            prev.next = curr.next
            curr.next = next_node
            prev = curr  
            curr = curr.next
        
        return dummy.next
                 

            
