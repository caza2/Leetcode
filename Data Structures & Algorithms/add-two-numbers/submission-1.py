# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumHead: ListNode = ListNode(val=(l1.val + l2.val)%10)
        curr: ListeNode = sumHead
        carry: int = (l1.val + l2.val)//10
        while l1.next and l2.next:
            l1 = l1.next
            l2 = l2.next
            curr.next = ListNode(val=((l1.val + l2.val + carry)%10))
            curr = curr.next
            carry = (l1.val + l2.val + carry)//10
        while l1.next:
            l1 = l1.next
            curr.next = ListNode(val=((l1.val + carry)%10))
            curr = curr.next
            carry = (l1.val + carry)//10
        while l2.next:
            l2 = l2.next
            curr.next = ListNode(val=((l2.val + carry)%10))
            curr = curr.next
            carry = (l2.val + carry)//10
        if carry:
            curr.next = ListNode(val=carry)
        return sumHead
