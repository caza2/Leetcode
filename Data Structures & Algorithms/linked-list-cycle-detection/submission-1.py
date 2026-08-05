# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None:
            return False
        hashSet: set[int] = set()
        leftNode: ListNode = head
        start: ListNode = head
        count: int = 0
        while head:
            if head.val in hashSet:
                temp_count: int = 0
                while temp_count < count:
                    if leftNode.val == head.val and leftNode == head:
                        return True
                    else:
                        leftNode = leftNode.next
                        temp_count += 1
                leftNode = start
            hashSet.add(head.val)
            head = head.next
            count += 1
        return False        