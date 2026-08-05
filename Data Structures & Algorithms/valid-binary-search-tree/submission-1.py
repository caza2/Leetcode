# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def getMaxNode(root: TreeNode) -> int:
            curr: TreeNode = root
            while curr.right:
                curr = curr.right
            return curr.val
            
        def getMinNode(root: TreeNode) -> int:
            curr: TreeNode = root
            while curr.left:
                curr = curr.left
            return curr.val
            
        if not root:
            return True
        return (
            self.isValidBST(root.left)
            and self.isValidBST(root.right)
            and (getMaxNode(root.left) < root.val if root.left else True)
            and (getMinNode(root.right) > root.val if root.right else True)
        )