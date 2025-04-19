'''
49. Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Here, n is the number of strings in strs, and k is the maximum length of a string in strs.
'''
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagram2(self, strs: List[str]) -> List[str]:      # Time - O(n * k log k), Space - O(n * k)
        res = defaultdict(list)

        for s in strs:

            res["".join(sorted(s))].append(s)
            
        return list(res.values())

    
    def groupAnagram(self, strs: List[str]) -> List[str]:       # Time - O(n * k), Space - O(n * k)
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:

                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        return list(res.values())


strs = ["act","pots","tops","cat","stop","hat"]
test = Solution()
w = test.groupAnagram(strs)
print(w)