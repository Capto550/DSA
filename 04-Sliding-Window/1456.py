"""
1456.Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen="aeiou"
        c=0
        for i in range(k):
            if s[i] in seen:
                c+=1
        maxi=c
        for right in range(k,len(s)):
            if s[right-k] in seen:
                c-=1
            if s[right] in seen:
                c+=1
            maxi=max(maxi,c)
        return maxi
