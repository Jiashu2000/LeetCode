# 239. Sliding Window Maximum

from typing import List
import heapq
from collections import deque
import MonotonicQueue

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []
        curMax = -10002
        left = 0
        n = len(nums)

        for right in range(n):
            if right - left + 1 <= k:
                num = nums[right]
                curMax = max(curMax, num)
                heapq.heappush(window, (-num, right))
            else:
                res.append(curMax)
                num = nums[right]
                heapq.heappush(window, (-num, right))
                left += 1
                while len(window) > 0 and window[0][1] < left:
                    heapq.heappop(window)
                if len(window) > 0: 
                    curMax = -window[0][0]
        res.append(curMax)
        return res
    
    '''
    time complexity: o(nlogn)
    space complexity: o(n)
    '''



    # using deque() instead of list
    # deque is more efficient. especially for popleft()

    def deque(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        n = len(nums)
        res = []
        left = 0
        
        for right in range(n):
            num = nums[right]
            if right - left + 1 <= k:
                while len(window) > 0 and num > window[-1]:
                    window.pop()
                window.append(num)
            else:
                res.append(window[0])
                # remove left num
                if nums[left] == window[0]:
                    window.popleft()
                left += 1 
                # add right num
                while len(window) > 0 and num > window[-1]:
                    window.pop()
                window.append(num)
        res.append(window[0])
        return res 
    
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''

    def queue_eg(self, nums: List[int], k: int) -> List[int]:
        queue = MonotonicQueue()
        result = []
        for i in range(k):
            queue.push(nums[i])
        result.append(queue.front())
        for i in range(k, len(nums)):
            queue.pop(nums[i-k]) # remove left element
            queue.push(nums[i]) # add right element
            result.append(queue.front())
        return result

    '''
    time complexity: o(n)
    space complexity: o(k)
    '''