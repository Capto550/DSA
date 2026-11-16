"""
61. Rotate list (Medium)
https://leetcode.com/problems/rotate-list
"""

class Solution(object):
    def rotateRight(self, head, k):

        if head is None or head.next is None:
            return head

        # Find length and tail
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Remove unnecessary rotations
        k = k % length

        if k == 0:
            return head

        # Make circular linked list
        tail.next = head

        # Find new tail
        steps = length - k - 1
        new_tail = head

        for i in range(steps):
            new_tail = new_tail.next

        # Find new head
        new_head = new_tail.next

        # Break the circle
        new_tail.next = None

        return new_head