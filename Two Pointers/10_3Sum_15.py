'''
15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].'''

from typing import List
class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:        # Time - O(n³), Space - O(m) [Where, m is the number of triplets]
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple([nums[i],nums[j],nums[k]]))
        return [list(i) for i in res]


    def threeSum(self, nums: List[int]) -> List[List[int]]:         # Time - O(n²), Space - O(m) [Where, m is the number of triplets]
        res = []
        nums.sort()
        for i, a in enumerate(nums):

            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums) - 1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
                while nums[l] == nums[l-1]:
                    l += 1
        return res


# Testing

test = Solution()
nums = [-1,0,1,2,-1,-4]
w = test.threeSum(nums)
print(w)
