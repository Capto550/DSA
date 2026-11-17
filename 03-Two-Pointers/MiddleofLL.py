"""
876. Middle of the Linked List(Easy)
https://leetcode.com/problems/middle-of-the-linked-list
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        itj=itr=head
        c=0
        while itr.next:
            c+=1
            itr=itr.next
        if c%2!=0:
            a=c//2
        
            for _ in range(a+1):
                itj=itj.next
            return itj
        else:
            a=c//2
            for _ in range(a):
                itj=itj.next
            return itj