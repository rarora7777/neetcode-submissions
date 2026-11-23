# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get size of list
        N = 0
        node = head
        while node:
            N += 1
            node = node.next
        
        # Remove head
        if N == n:
            return head.next

        i = 1
        node = head
        while i < N-n:
            i += 1
            node = node.next
        
        node.next = node.next.next

        return head
        