'''
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''

class Solution:

    def characterReplacement2(self, s: str, k: int) -> int:         # Time - O(n), Space - O(1)
        count = {}
        res, l = 0, 0

        for r in range(len(s)):

            c = s[r]
            count[c] = count.get(c,0) + 1

            if (r - l + 1) - max(count.values()) <= k:
                res = max(res,r-l+1)

            else:
                count[s[l]] = count[s[l]] - 1
                l += 1

        return res
    
    def characterReplacement(self, s: str, k: int) -> int:          # Time - O(n), Space - O(1)
        count = {}
        res, l = 0, 0

        for r in range(len(s)):

            c = s[r]
            count[c] = count.get(c,0) + 1

            while (r-l+1) - max(count.values()) > k:

                count[s[l]] -= 1
                l += 1

            res = max(res,r-l+1)

        return res
            

test = Solution()
s = "AABABBA"
k = 1
w = test.characterReplacement(s, k)
print(w)