"""
2461. Maximum Sum of Distinct Subarrays With Length K

https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
"""
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        left = 0
        curr_sum = 0
        maxi = 0
        s = set()

        for right in range(len(nums)):

            # If duplicate exists, shrink until it is removed
            while nums[right] in s:
                s.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Add current element
            s.add(nums[right])
            curr_sum += nums[right]

            # Maintain window size k
            if right - left + 1 > k:
                s.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Check valid window
            if right - left + 1 == k:
                maxi = max(maxi, curr_sum)

        return maxi
