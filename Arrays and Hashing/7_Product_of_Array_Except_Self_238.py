'''
LeetCode 238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = 1, 1
        res = []

        for i in range(len(nums)):

            res.append(prefix)
            prefix *= nums[i]

        for  j in range(len(nums)-1,-1,-1):
            
            res[j] *= postfix
            postfix *= nums[j]
        
        return res

# Testing

nums = [-1,1,0,-3,3]
test = Solution()
w = test.productExceptSelf(nums)
print(w)