# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'))
        curr = dummy


        while True:
            curr_min = (dummy, -1)

            for i, node in enumerate(lists):
                if node and node.val < curr_min[0].val:
                    curr_min = (node, i)
            
            if curr_min[1] == -1:
                break
    
            curr.next = curr_min[0]
            curr = curr.next
            lists[curr_min[1]] = lists[curr_min[1]].next
        
        return dummy.next