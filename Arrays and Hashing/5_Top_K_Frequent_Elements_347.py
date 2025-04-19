'''
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

'''
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k:int) -> List[int]:    # Time - O(n), Space - O(n)

        res = []
        freq = [[] for _ in range(len(nums))]
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        for val, cnt in count.items():
            freq[cnt].append(val)
        
        for i in range(len(freq)-1,0,-1):

            for val in freq[i]:
                res.append(val)

                if len(res) == k:  
                    return res
                
        return
    

nums = [1,1,1,2,2,3,7,7,7,7]
k = 2
test = Solution()
w = test.topKFrequent(nums,k)
print(w)