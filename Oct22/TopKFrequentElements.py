# 347. Top K Frequent Elements

from typing import List
import heapq


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for i in nums:
            count_map[i] = count_map.get(i, 0) + 1
        
        queue = []
        for n, v in count_map.items():
            heapq.heappush(queue, (-v, n))
        res = []
        while k > 0:
            pop = heapq.heappop(queue)
            res.append(pop[1])
            k -= 1
        return res

'''
time complexity: o(nlogn)
space complexity: o(n)
'''