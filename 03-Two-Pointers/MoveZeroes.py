"""
283.Move Zeroes(Easy)
https://leetcode.com/problems/move-zeroes
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        for i in nums[:]:
            if i==0:
                nums.remove(i)
                l+=1
        for i in range(l):
            nums.append(0)
        return nums