# 454. 4SumII

from typing import List
from collections import defaultdict

class Solution:

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        map = defaultdict(lambda: 0)
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                subsum = nums1[i] + nums2[j]
                map[subsum] += 1
        
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                subsum = nums3[i] + nums4[j]
                if -subsum in map:
                    res += map[-subsum]
        return res


'''
time complexity: o(n^2)
space complexity:o(n^2)
'''

        
        
        