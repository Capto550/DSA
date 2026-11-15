"""
15. 3Sum  (Medium)
https://leetcode.com/problems/3sum/

Approach: sort + fix one number, then two pointers on the rest.
Skip duplicates for both the fixed number and the pointers.

Time:  O(n^2)
Space: O(1) excluding output
"""

def threesum(self,nums):
    nums.sort()
    res=[]
    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=len(nums)-1
        while l<r:
            total=nums[i]+nums[l]+nums[r]
            if total<0:
                l+=1
            elif total>0:
                r-=1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
    return res