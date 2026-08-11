# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        def reverseLL(head: ListNode) -> ListNode:
            prev, curr = None, head

            while curr:
                nxt, curr.next = curr.next, prev
                prev, curr = curr, nxt

            return prev

        curr = head
        breakLeft = head
        count: int = 1
        NodeList: list[ListNode] = []
        while curr.next:
            if count % k:
                curr = curr.next
                count += 1
            else:
                temp = curr.next
                curr.next, curr = None, temp
                NodeList.append(reverseLL(breakLeft))
                breakLeft = temp
                count += 1

        if count % k:
            NodeList.append(breakLeft)
        else:
            NodeList.append(reverseLL(breakLeft))

        head = NodeList[0]
        for i in range(len(NodeList)-1):
            curr = NodeList[i]
            while curr.next:
                curr = curr.next
            curr.next = NodeList[i+1]
        
        return head


