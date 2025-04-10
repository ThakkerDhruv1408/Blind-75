'''Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
'''
nums = [3,4,5,6]
target = 8
hashmap = {}

for i, val in enumerate(nums):
    diff = target - val
    if diff in hashmap:
        print([hashmap[diff],i])
        break
    hashmap[val] = i
