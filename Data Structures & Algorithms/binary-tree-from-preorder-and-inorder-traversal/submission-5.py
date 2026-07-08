# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}  # store each value's index in inorder so we can find it in O(1)

        def builder(pre_start, pre_end, in_start, in_end):  # builds one subtree using slices of preorder and inorder
            if pre_start > pre_end:  # no elements left in this range, so there is no node
                return None

            root = preorder[pre_start]  # the first value left in preorder is always the current root
            mid = inorder_map[root]  # find that root's position inside the inorder range
            left_size = mid - in_start  # everything left of mid in inorder belongs to the left subtree

            node = TreeNode(root)  # create the node for this root value
            node.left = builder(pre_start + 1, pre_start + left_size, in_start, mid - 1)  # next left_size values in preorder build the left subtree
            node.right = builder(pre_start + left_size + 1, pre_end, mid + 1, in_end)  # the rest of preorder builds the right subtree

            return node  # hand this completed subtree back to the caller

        return builder(0, len(preorder) - 1, 0, len(inorder) - 1)  # start the recursion covering the whole arrays