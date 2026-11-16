"""
167. Two Sum II - Input Array Is Sorted(Medium)
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        sum=0
        q=[]
        while l<r:
            sum=numbers[l] + numbers[r]
            if sum==target:
                q.append(l+1)
                q.append(r+1)
                break
            elif sum<=target:
                l=l+1
            else:
                r=r-1
        return q