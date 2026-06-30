# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ordered = []
        res = []

        def levels(root, i):
            if not root:
                return
            if len(ordered) < i:
                ordered.append([root.val])
            else:
                ordered[i-1].append(root.val)
            
            levels(root.right, i+1)
            levels(root.left, i+1)

        levels(root, 1)

        for level in ordered:
            res.append(level[0])
        
        return res