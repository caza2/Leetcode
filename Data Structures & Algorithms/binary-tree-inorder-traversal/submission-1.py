# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output: list[int] = []
        stack: list[tuple[TreeNode, bool]] = [(root, False)]
        while stack:
            tempNode, leftVisited = stack.pop()
            if not tempNode:
                continue
            if not leftVisited:
                stack.append((tempNode, True))
                stack.append((tempNode.left, False))
            else:
                output.append(tempNode.val)
                stack.append((tempNode.right, False))
        return output