# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes: int = 0
        dfsStack: list[tuple[Optional[TreeNode], bool, bool]] = [(root, False, False)]
        upStack: list[int] = []
        while dfsStack:
            tempNode, seenLeft, seenRight = dfsStack.pop()
            if not tempNode:
                continue
            if not seenLeft:
                dfsStack.append((tempNode, True, False))
                if not upStack or tempNode.val >= upStack[-1]:
                    upStack.append(tempNode.val)
                    goodNodes += 1
                dfsStack.append((tempNode.left, False, False))
            elif not seenRight: # a été vu à gauche du coup
                dfsStack.append((tempNode, True, True))
                dfsStack.append((tempNode.right, False, False))
            else:
                if upStack[-1] == tempNode.val:
                    upStack.pop()
        return goodNodes