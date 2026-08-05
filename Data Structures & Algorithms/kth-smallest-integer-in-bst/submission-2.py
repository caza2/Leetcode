# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #k-th element du inorder traversal !
        stack: list[tuple[Optional[TreeNode], bool, bool]] = [(root, False, False)]
        output: list[int] = []
        while len(output) < k: # On suppose que le problème est bien paramétré et que k < taille de l'arbre)
            tempNode, seenLeft, seenRight = stack.pop()
            if not tempNode:
                continue
            if not seenLeft:
                stack.append((tempNode, True, False))
                stack.append((tempNode.left, False, False))
            elif not seenRight:
                stack.append((tempNode, True, True))
                output.append(tempNode.val)
                stack.append((tempNode.right, False, False))
        return output[-1]