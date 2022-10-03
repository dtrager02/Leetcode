# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        curr = None
        while list1 or list2:
            if not list1:
                smaller = list2
            elif not list2:
                smaller = list1
            elif list1.val > list2.val:
                smaller = list2
            else:
                smaller = list1
            if not curr:
                newList = ListNode(smaller.val,smaller.next)
                curr = newList
            else:
                curr.next = ListNode(smaller.val,smaller.next)
                curr = curr.next
            if smaller is list2:
                list2 = list2.next
            else:
                list1 = list1.next
        return newList
                
                
                