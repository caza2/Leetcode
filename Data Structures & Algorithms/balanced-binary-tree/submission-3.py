# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced: bool = True
        def depth(root: Optional[TreeNode]) -> int:
            nonlocal isBalanced
            if not root:
                return 0
            leftHeight, rightHeight = depth(root.left), depth(root.right)
            if abs(leftHeight - rightHeight) > 1:
                isBalanced = False
            return 1 + max(leftHeight, rightHeight)
        _: int = depth(root)
        return isBalanced