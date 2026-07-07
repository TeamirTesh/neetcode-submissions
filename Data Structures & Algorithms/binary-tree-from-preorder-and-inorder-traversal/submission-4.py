# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def builder(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            root = preorder[pre_start]
            mid = inorder_map[root]
            left_size = mid - in_start

            node = TreeNode(root)
            node.left = builder(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            node.right = builder(pre_start + left_size + 1, pre_end, mid + 1, in_end)

            return node

        return builder(0, len(preorder) - 1, 0, len(inorder) - 1)