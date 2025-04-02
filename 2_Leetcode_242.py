'''
Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}

        for i in range(len(s)):
            counter[s[i]] = counter.get(s[i],0) + 1
            counter[t[i]] = counter.get(t[i],0) - 1
        
        return all(value == 0 for value in counter.values())
