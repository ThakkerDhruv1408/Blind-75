'''
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.
'''

class Solution:
    def validPalindrom2(self, s: str) -> bool:          # Time - O(n), Space - O(n)
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c
        return newstr[::-1].lower() == newstr.lower()


    def validPalindrom(self, s: str) -> bool:           # Time - O(n), Space - O(1)
        l, r = 0, len(s)-1
        while l < r:
            while not self.isalphanum(s[l]) and l<r:
                l += 1
            while not self.isalphanum(s[r]) and r>l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


    
    def isalphanum(self, s: chr) -> bool:
        return (ord("A") <= ord(s) <= ord("Z") or
                ord("a") <= ord(s) <= ord("z") or
                ord("0") <= ord(s) <= ord("9")
                )

# Testing

test = Solution()
s = "A man, a plan, a canal: Panama"
t = ""
w = test.validPalindrom(s)
print(w)