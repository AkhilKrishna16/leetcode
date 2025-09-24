# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find the middle, reverse everything from that point
        # then have the two pointers again, and add up everything until fast 
        # reaches the end

        middle = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = middle
            middle = middle.next
        prev = None
        curr = middle
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # add the sums
        curr_sum = 0
        first = head
        ret = float('-inf')
        while prev:
            curr_sum = first.val + prev.val
            ret = max(ret, curr_sum)
            first = first.next
            prev = prev.next
        
        return ret



            