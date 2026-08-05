# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output: list[int] = []
        if not root:
            return output
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

