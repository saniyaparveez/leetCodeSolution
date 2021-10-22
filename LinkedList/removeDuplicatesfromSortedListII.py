# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        if head.val != head.next.val: 
            head.next = self.deleteDuplicates(head.next)
            return head
        
        cur = head
        while cur.next and cur.next.val == cur.val:
            cur = cur.next
    
        return self.deleteDuplicates(cur.next)
        
