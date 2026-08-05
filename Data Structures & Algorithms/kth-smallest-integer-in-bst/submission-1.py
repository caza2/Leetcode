# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #k-th element du inorder traversal !
        def inOrderTraversal(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return []
            else:
                return inOrderTraversal(root.left) + [root.val] + inOrderTraversal(root.right)
        inOrder: list[int] = inOrderTraversal(root)
        return inOrder[k-1]