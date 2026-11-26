"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for char in s1:
            need[char] = need.get(char, 0) + 1

        k = len(s1)

        for i in range(k):
            window[s2[i]] = window.get(s2[i], 0) + 1

        if need == window:
            return True

        for i in range(k, len(s2)):

            # Remove outgoing character
            left_char = s2[i-k]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            # Add incoming character
            right_char = s2[i]
            window[right_char] = window.get(right_char, 0) + 1

            if need == window:
                return True

        return False
