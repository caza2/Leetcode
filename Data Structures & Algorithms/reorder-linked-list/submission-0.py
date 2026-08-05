# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Compter taille linked list
        _len: int = 0
        curr: ListNode = head
        while curr:
            _len += 1
            curr = curr.next
        # Couper la liste en deux au milieu
        left: ListNode = head
        _count: int = 0
        while _count < _len//2:
            _count += 1
            left = left.next
        right = left.next
        left.next = None
        # Revert la liste de droite
        prev, curr = None, right
        while curr:
            temp: ListeNode = curr.next
            curr.next = prev
            prev, curr = curr, temp
        right = prev
        # Merge les deux listes
        while right and head:
            temp: ListNode = head.next
            head.next = right
            right = right.next
            head = head.next
            head.next = temp
            head = head.next