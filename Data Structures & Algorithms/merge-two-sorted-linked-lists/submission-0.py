# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2 if list2 else None

        elif not list2:
            return list1 if list1 else None
        
        elif list1.val > list2.val:
            list1, list2 = list2, list1
        
        head = list1
        
        while list1 and list2:
            list1_next = list1.next.val if list1.next else float('inf')
            if list2.val >= list1.val and list2.val <= list1_next:
                temp1 = list1.next
                temp2 = list2.next

                list1.next = list2
                list2.next = temp1

                list1 = list1.next
                list2 = temp2
            
            elif list1.next:
                list1 = list1.next

            else:
                break

        while list2:
            list1.next = list2
            list2 = list2.next
        
        return head
