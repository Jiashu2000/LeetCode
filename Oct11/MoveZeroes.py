# 283. Move Zeroes


from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        slow, fast = 0, 0
        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        for i in range(slow, n):
            nums[i] = 0

    '''
    time complexity: o(n)
    space complexity: o(1)
    '''