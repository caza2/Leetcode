# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        _len: int = 0
        count: ListNode = head
        while count:
            _len += 1
            count = count.next
        index: int = 0
        bypass: int = _len - 1 - n
        if bypass == -1:
            return head.next
        curr: ListNode = head
        while index != bypass:
            index += 1
            curr = curr.next
        curr.next = curr.next.next
        return head