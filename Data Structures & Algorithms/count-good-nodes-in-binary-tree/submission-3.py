# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        greatest = root
        def goods(root, greatest):
            if not root:
                return None
            if root.val >= greatest.val:
                greatest = root
            
            if root == greatest:
                res.append(root)
            
            goods(root.left, greatest)
            goods(root.right, greatest)

        goods(root, greatest)
        
        return len(res)

