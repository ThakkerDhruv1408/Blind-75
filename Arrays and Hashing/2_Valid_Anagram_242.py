'''
LeetCode 242. Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
'''

from collections import Counter
class Solution:
    def isAnagram2(self, s: str, t: str) -> bool:           # Time - O(n log n), Space - O(n)
        return sorted(s) == sorted(t)
    

    def isAnagram1(self, s: str, t: str) -> bool:           # Time - O(n), Space - O(1)
        return Counter(s) == Counter(t)
    

    def isAnagram(self, s: str, t: str) -> bool:            # Time - O(n), Space - O(1)
        
        if len(s) != len(t):
            return False
        
        counter = {}

        for i in range(len(s)):
            
            counter[s[i]] = counter.get(s[i],0) + 1
            counter[t[i]] = counter.get(t[i],0) - 1
        
        return all(value == 0 for value in counter.values())

    
# Testing

test = Solution()
x, y = "meow" , "omew"
w = test.isAnagram2(x, y)
print(w)