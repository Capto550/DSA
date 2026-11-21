"""
3. Longest Substring Without Repeating Characters(Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        seen=set()
        maxi=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi