"""
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        w=sum(nums[:k])
        m=w
        for i in range(k,len(nums)):
            w+=nums[i]
            w-=nums[i-k]

            m=max(m,w)
        return float(m)/k            