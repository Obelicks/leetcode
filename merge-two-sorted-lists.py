# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #base cases
        if not list1:
            return list2
        if not list2:
            return list1
        #make head
        if list1.val < list2.val: 
            head = list1
            list1 = head.next
        else: 
            head = list2
            list2 = head.next
        current = head
        while list2 or list1:
            if not list1:
                current.next = list2
                break
            if not list2:
                current.next = list1
                break
            if list2.val > list1.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        return head
