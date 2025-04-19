'''
LeetCode 217. Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''
from typing import List
class Solution:
    def hasDuplicate2(self, nums: List[int]) -> bool:   # Time - O(n²)   Space - O(1)

        for i in range(len(nums)):

            for j in range(i+1, len(nums)):

                if nums[i] == nums[j]:
                    return True
                
        return False

    
    def hasDuplicate(self, nums: List[int]) -> bool:    # Time - O(n)   Space - O(n)
        hashset = set()

        for i in nums:

            if i in hashset:
                return True
            
            hashset.add(i)
            
        return False
    
# Testing
n = [1,2,5,7,9,7]
test = Solution()
w = test.hasDuplicate(n)
print(w)