# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1: ListNode | None , list2: ListNode) -> ListNode:
            curr: ListNode = ListNode()
            newList: ListNode = curr
            while list1 and list2:
                if list1.val < list2.val:
                    temp, list1 = list1, list1.next
                    temp.next, curr.next = None, temp
                    curr = curr.next
                else:
                    temp, list2 = list2, list2.next
                    temp.next, curr.next = None, temp
                    curr = curr.next
            if list1:
                curr.next = list1
            else:
                curr.next = list2
            return newList.next
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            middle = len(lists)//2
            return merge(self.mergeKLists(lists[middle:]), self.mergeKLists(lists[:middle]))