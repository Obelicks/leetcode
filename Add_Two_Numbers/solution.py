class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        base = 1
        carry = 0
        while (l1 != None) and (l2 != None):
            if base ==1:
                base = 0
                solution = ListNode()
                placer = solution
            else: 
                placer.next = ListNode()
                placer = placer.next
            val = l1.val + l2.val + carry 
            if val >= 10: carry = 1
            else : carry = 0
            placer.val = val%10
            l1 = l1.next; l2 = l2.next
        return(solution)
        