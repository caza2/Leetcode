# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSimilar(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSimilar(p.left, q.left) and isSimilar(p.right, q.right)
        
        queue: deque = deque()
        queue.append(root)
        while queue:
            tempNode = queue.popleft()
            if not tempNode:
                continue
            if tempNode.val == subRoot.val and isSimilar(tempNode, subRoot):
                return True
            queue.append(tempNode.left)
            queue.append(tempNode.right)
        return False
                