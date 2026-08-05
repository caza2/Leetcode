"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy: Node = Node(head.val)
        start: Node = copy
        curr: Node = head
        hashMap_original: dict[Node, int] = dict()
        hashMap_copy: dict[int, Node] = dict()
        _count: int = 0
        while curr:
            if curr.next:
                copy.next = Node(curr.next.val)
            else:
                copy.next = None
            hashMap_original[curr] = _count
            hashMap_copy[_count] = copy
            copy = copy.next
            curr = curr.next
            _count += 1
        copy = start
        curr = head
        while curr:
            if curr.random:
                copy.random = hashMap_copy[hashMap_original[curr.random]]
            else:
                copy.random = None
            curr = curr.next
            copy = copy.next
        return start