# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.are_equal = True
        def compare(p, q):
            p_val = p.val if p else float('inf')
            q_val = q.val if q else float('inf')
            
            if p_val != q_val:
                self.are_equal = False

            if p and q:
                compare(p.left, q.left)
                compare(p.right, q.right)
        
        compare(p, q)
        return self.are_equal