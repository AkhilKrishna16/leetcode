# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []
        p = True
        
        slow = head
        while slow:
            st.append(slow)
            slow = slow.next

        j = head
        while head:
            val = st.pop()
        
            if val.val == head.val:
                head = head.next
            else:
                return False
        
        return True
        
        
