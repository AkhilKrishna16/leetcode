# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # go through the groups such as 1, 2, 3, 4...
        # have a while loop that runs while you have head
        # iterate through and get the count of the current group (max(group, len(sublist)))
        # if not even, skip through else
        # go through and reverse each node within the list from the start
        # and then attach con to the prev and the tail to the next node
        

        group_size = 1
        node = head
        dummy = ListNode(0, head)
        prev_group_tail = dummy

        while node:
            # Step 1. Count how many nodes exist in this group
            count = 0
            group_head = node
            while node and count < group_size:
                node = node.next
                count += 1
            group_tail_next = node    # node after this group

            # Step 2. Reverse the group if its length is even
            if count % 2 == 0:
                curr = group_head
                prev = group_tail_next   # reversed group's tail should connect here
                for _ in range(count):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt

                # After reversal:
                # prev = new head of this group
                # group_head = new tail of this group
                prev_group_tail.next = prev
                prev_group_tail = group_head
            else:
                # If not reversed, just move prev_group_tail to the end of this group
                prev_group_tail = group_head
                for _ in range(count - 1):
                    prev_group_tail = prev_group_tail.next

            # Step 3. Move to next group
            group_size += 1

        return dummy.next