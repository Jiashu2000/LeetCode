# 209. Minimum Size Subarray Sum



'''
sliding window: 滑动窗口

不断的调节子序列的起始位置和终止位置

窗口内是什么？满足和 >=s 的长度最小的连续子数组
如何移动窗口的起始位置？如果当前窗口的值大于s, 窗口需要向前移动
如何移动窗口的结束位置？窗口的结束位置就是遍历数组的指针，也就是for循环的索引

时间复杂度为什么是o(n)？
每个元素在滑动窗口进来操作一次，出去操作一次，时间复杂度是2*n, o(n)
'''

from typing import List


class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        left = 0
        i = 0
        window = 0

        while i < n:
            while i < n and window < target:
                window += nums[i]
                i += 1
                
            while left < i and window >= target:
                min_len = min(i - left, min_len)
                window -= nums[left]
                left += 1
        
        if min_len  == n + 1:
            return 0
        return min_len


