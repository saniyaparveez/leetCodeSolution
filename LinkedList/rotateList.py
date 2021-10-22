# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        
        last = head
        count = 1
        while last.next:
            count += 1
            last = last.next
        
        last.next = head
        curr = head
        
        for _ in range(count - (k % count) - 1):
            curr = curr.next
        
        res = curr.next
        curr.next = None
        
        return res
