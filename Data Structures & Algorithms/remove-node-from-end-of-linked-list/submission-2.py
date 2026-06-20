# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n==0:
            return head
        
        elif not head.next and n == 1:
            return None
        
        curr = behind = head
        dummy = ListNode(0, head)
        prev = dummy

        for i in range(n-1):
            if curr.next:
                curr = curr.next
            else:
                break

        while curr.next:
            curr = curr.next
            behind = behind.next
            prev = prev.next

        if behind == head:
            head = head.next
        else:
            prev.next = behind.next

        return head
        
        