# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def levels(root, i):
            if not root:
                return
            if len(res) < i:
                res.append([root.val])
            else:
                res[i-1].append(root.val)
            
            levels(root.left, i+1)
            levels(root.right, i+1)
        
        levels(root, 1)
        return res