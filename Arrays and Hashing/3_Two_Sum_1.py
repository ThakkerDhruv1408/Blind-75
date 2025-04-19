'''
1. Two Sum

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input   :   nums = [3,4,5,6], target = 7
Output  :   [0,1]
'''

from typing import List
class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:         # Time - O(n²)   Space - O(1)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []


    def twoSum(self, nums: List[int], target: int) -> List[int]:       # Time - O(n)   Space - O(n)
        hashmap = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[v] = i
        return[]



s = [1,2,5,77,9,11]
t = 78
# s = "jar", t = "jam"
test = Solution()
w = test.twoSum2(s,t)
print(w)

