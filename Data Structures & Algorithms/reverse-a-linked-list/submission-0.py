# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # Variable to keep track of previous node
        curr = head # Variable to keep track of current node

        while curr: # While loop to break when curr is None
            nxt = curr.next # Temporarily store the next node
            curr.next = prev # Point current node to previous node (reversing)
            prev = curr # Update current node to "prev" before moving on
            curr = nxt # Move current pointer to next node
        
        return prev # Return prev since it is 1 behind curr, and curr will end after it
                    # surpasses the tail node and becomes None
            
        