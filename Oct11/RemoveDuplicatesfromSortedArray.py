# 26. Remove Duplicates from Sorted Array

from typing import List

class Solution:

    # fast pointer: find new element
    # slow pointer: location to be replaced
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        fast, slow = 1, 1
        prev = nums[0]
        while fast < n:
            if nums[fast] != prev:
                prev = nums[fast]
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
    
    '''
    time complexity: o(n)
    space complexity: o(1)
    '''