from collections import deque

class TreeNode:
    def __init__(self, val: list[int], left: Optional[TreeNode] = None, right: Optional[TreeNode] = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        root: Optional[TreeNode] = TreeNode(val=[])
        curr: Optional[TreeNode] = root
        queue: deque = deque()
        queue.append(root)
        for i in range(len(nums)):
            for _ in range(len(queue)):
                tempNode: Optional[TreeNode] = queue.popleft()
                tempLeft: Optional[TreeNode] = TreeNode(val=tempNode.val + [nums[i]])
                tempRight: Optional[TreeNode] = TreeNode(val=tempNode.val)
                queue.append(tempLeft)
                queue.append(tempRight)
        output: list[int] = []
        while queue:
            output.append(queue.popleft().val)
        return output