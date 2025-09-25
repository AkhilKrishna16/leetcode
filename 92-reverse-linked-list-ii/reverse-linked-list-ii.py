# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        con = prev
        tail = curr
        new_prev = None

        j = 0
        while j < right - left + 1 and curr:
            next_node = curr.next
            curr.next = new_prev
            new_prev = curr
            curr = next_node
            j += 1

        if con:
            con.next = new_prev
        else:
            head = new_prev
        if tail:
            tail.next = curr
        return head