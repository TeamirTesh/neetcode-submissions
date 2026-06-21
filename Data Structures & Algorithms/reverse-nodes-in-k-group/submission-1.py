# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode()
        group_prev = dummy

        l = head
        while l:
            # find the k-th node from l
            r = l
            for _ in range(k - 1):
                if not r:
                    break
                r = r.next

            if not r:
                # fewer than k nodes left, attach as-is
                group_prev.next = l
                break

            # reverse the group [l, r]
            next_group_start = r.next
            prev = next_group_start
            curr = l
            while curr != next_group_start:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            group_prev.next = r       # r is now the head of the reversed group
            group_prev = l            # l is now the tail of the reversed group
            l = next_group_start

        return dummy.next



                    



                