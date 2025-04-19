'''
LeetCode 3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> str:       # Time - O(n), Space - O(n)
        
        res, l = 0, 0
        charset = set()

        for r in range(len(s)):

            while s[r] in charset:

                charset.remove(s[l])
                l += 1

            charset.add(s[r])
            res = max(res,(r-l+1))
            
        return res
    
# Testing

test = Solution()
s = "abcdefghijklmnopqrstuvwxyz"
w = test.lengthOfLongestSubstring(s)
print(w)
            
            
            

