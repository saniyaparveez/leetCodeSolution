# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        carry = 0
        dummyList = ListNode(0)
        curr = dummyList
        
        while p1 or p2:
            x = 0
            y = 0
            if p1 != None:
                x = p1.val
                p1 = p1.next
            if p2 != None:
                y = p2.val
                p2 = p2.next
            
            summ = carry + x + y
            carry = summ // 10
            curr.next = ListNode(summ % 10)
            curr = curr.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummyList.next
            
            
        