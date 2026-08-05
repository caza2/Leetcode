# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr: Optional[TreeNode] = root
        if not curr:
            return TreeNode(val=val)
        while curr:
            if val >= curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val=val)
                    return root
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val=val)
                    return root
        
