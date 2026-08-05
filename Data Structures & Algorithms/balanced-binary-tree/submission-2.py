# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depthNode(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(depthNode(root.left), depthNode(root.right))
        if not root:
            return True
        depth_left, depth_right = depthNode(root.left), depthNode(root.right)
        if abs(depth_left - depth_right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False