# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        curr: ListNode | None = head
        right: ListNode | None = head.next
        curr.next = None
        while right.next != None:
            temp = right.next
            right.next = curr
            curr, right = right, temp
        right.next = curr
        return right