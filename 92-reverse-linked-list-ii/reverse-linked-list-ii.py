# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        left_point = head
        for _ in range(1, left):
            prev = left_point
            left_point = left_point.next
        con = prev
        tail = left_point
        new_prev = None
        j = 0
        while j < right - left + 1 and left_point:
            next_node = left_point.next
            left_point.next = new_prev
            new_prev = left_point
            left_point = next_node
            j += 1
        
        if con:
            con.next = new_prev
        else:
            head = new_prev
        if tail:
            tail.next = left_point
        return head