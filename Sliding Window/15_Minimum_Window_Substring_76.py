'''
LeetCode 76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Where n is the length of the string s and m is the total number of unique characters in the strings t and s.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:         # Time - O(n), Space - O(m)

        if t == "" : return ""
        
        l = 0
        res, reslen = [-1,-1], float("infinity")
        window, countT = {}, {}

        for c in t:

            countT[c] = countT.get(c,0) + 1
        
        have, need = 0, len(countT)

        for r in range(len(s)):

            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:

                if r-l+1 < reslen:

                    res = [l,r]
                    reslen = min(reslen,r - l + 1)

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res

        return s[l:r+1] if reslen != float("infinity") else ""
            


# Testing

test = Solution()
s = "cabwefgewcwaefgcf"
t = "cae"
w = test.minWindow(s, t)
print(w)