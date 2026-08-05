# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Queue:
    def __init__(self) -> None:
        self.data = deque()

    def __bool__(self) -> bool:
        return bool(self.data)
    
    def enqueue(self, node: Optional[TreeNode]) -> None:
        self.data.append(node)
    
    def dequeue(self) -> Optional[TreeNode]:
        return self.data.popleft()

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        parentQueue: Queue = Queue() # Queue pour BFS
        childQueue: Queue = Queue()
        depth: int = 0
        parentQueue.enqueue(root)
        while parentQueue:
            depth += 1
            while parentQueue:
                lastNode: TreeNode = parentQueue.dequeue()
                if not lastNode.right and not lastNode.left:
                    pass
                elif not lastNode.right:
                    childQueue.enqueue(lastNode.left)
                elif not lastNode.left:
                    childQueue.enqueue(lastNode.right)
                else:
                    childQueue.enqueue(lastNode.left)
                    childQueue.enqueue(lastNode.right)
            parentQueue, childQueue = childQueue, Queue()
        return depth