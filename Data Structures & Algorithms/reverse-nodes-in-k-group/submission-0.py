# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        section_tail = dummy
        l = r = head

        while l:
            r = l
            r_moves = 0
            while r and r_moves < k-1:
                r = r.next
                r_moves += 1

            if r_moves < k-1 or not r:
                section_tail.next = l
                l = r
            
            else:
                prev = None
                stop = r.next
                section_tail.next = r
                section_tail = l
                section_tail_nxt = r.next
                while l != stop:
                    nxt = l.next
                    l.next = prev
                    prev = l
                    l = nxt
                
                l = section_tail_nxt
    
        return dummy.next



                    



                