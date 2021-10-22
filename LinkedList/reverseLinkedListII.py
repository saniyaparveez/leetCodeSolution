# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if (head.next == None and left == 1 and right == 1):
            return head
        
        if left == right:
            return head
        
        lastNode = head
        for i in range(right):
            lastNode = lastNode.next
        
        start = None
        curr = head
        for i in range(1, left):
            start = curr
            curr = curr.next

        prev = lastNode
        for i in range(left, right+1):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
                
        if start == None:
            head = prev
        else:
            start.next = prev
        
        return head
