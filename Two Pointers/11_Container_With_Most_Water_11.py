'''
LeetCode 11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
'''
from typing import List

class Solution:
    def maxArea2(self, height: List[int]) -> int:           # Time - O(n²), Space - O(1)
        res = 0

        for i in range(len(height)-1):

            for j in range(i+1, len(height)):

                res = max(res, (min(height[i], height[j]) * (j-i)))

        return res


    def maxArea(self, height: List[int]) -> int:            # Time - O(n), Space - O(1)
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            
            area = min(height[l], height[r]) * (r-l)
            res = max(res, area)

            if height[l] < height[r]:
                l += 1

            else:
                r -= 1

        return res

# Testing

test = Solution()
nums = [1,8,6,2,5,4,8,3,7]
w = test.maxArea2(nums)
print(w)
