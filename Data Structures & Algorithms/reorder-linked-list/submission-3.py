# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        slow = fast = head
        prev = ListNode()
        prev.next = slow

        while fast.next:
            slow = slow.next
            prev = prev.next
            fast = fast.next.next if fast.next.next else fast.next


        prev.next = None
        prev = None

        while slow:
            ahead = slow.next
            slow.next = prev
            prev = slow
            if ahead:
                slow = ahead
            else:
                break

        left, right = head, prev

        while left and right:
            ahead_l = left.next
            ahead_r = right.next

            left.next = right
            if ahead_l:
                right.next = ahead_l

            left = ahead_l
            right = ahead_r
    
    
        