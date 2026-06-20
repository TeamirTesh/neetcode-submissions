# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        for _ in range(n):
            curr = curr.next

        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next

        return dummy.next
        
        