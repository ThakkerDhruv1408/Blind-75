'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
'''
from collections import defaultdict
class Solution:
    def groupAnagram(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

class Solution2:
    def groupAnagram(self, strs):
        res = defaultdict(list)

        for s in strs:
            res["".join(sorted(s))].append(s)
        return list(res.values())