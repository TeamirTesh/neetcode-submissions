"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = dict()
        curr = head

        while curr:
            if curr.next not in copies:
                new_next = Node(curr.next.val) if curr.next else None
                copies[curr.next] = new_next
            else:
                new_next = copies[curr.next]

            if curr.random not in copies:
                new_random = Node(curr.random.val) if curr.random else None
                copies[curr.random] = new_random
            else:
                new_random = copies[curr.random]
            
            if curr not in copies:
                new = Node(curr.val, new_next, new_random)
                copies[curr] = new
            else:
                copies[curr].next = new_next
                copies[curr].random = new_random

            curr = curr.next

        

        if copies:
            return copies[head]
        else:
            return None

