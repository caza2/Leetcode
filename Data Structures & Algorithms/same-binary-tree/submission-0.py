# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sameStructure: bool = True
        if not p and not q:
            return True
        def sameSubtree(p: Optional[TreeNode], q: Optional[TreeNode]) -> None:
            nonlocal sameStructure
            if (p and not q) or (q and not p):
                sameStructure = False
            if (p and q) and (p.val != q.val):
                sameStructure = False
            if (p and q) and ((p.right and not q.right) or (q.right and not p.right)):
                sameStructure = False
            if (p and q) and ((p.left and not q.left) or (q.left and not p.left)):
                sameStructure = False
            if (p and q) and (p.right and q.right):
                sameSubtree(p.right, q.right)
            if (p and q) and (p.left and q.left):
                sameSubtree(p.left, q.left)
        sameSubtree(p, q)
        return sameStructure