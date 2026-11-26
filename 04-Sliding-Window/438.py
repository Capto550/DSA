"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string
"""
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_count = {}
        window = {}

        # Count characters in p
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        left = 0
        result = []
        k = len(p)

        for right in range(len(s)):

            # Add incoming character
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Maintain window size k
            if right - left + 1 > k:
                old = s[left]
                window[old] -= 1

                if window[old] == 0:
                    del window[old]

                left += 1

            # Compare frequencies
            if window == p_count:
                result.append(left)

        return result
