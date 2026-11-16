"""
234.Palindrome Linked List(Easy)
https://leetcode.com/problems/palindrome-linked-list
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        self.head=head
        l=''
        itr=self.head
        while itr:
            l+=str(itr.val)
            itr=itr.next
        if l==l[::-1]:
            return True
        return False