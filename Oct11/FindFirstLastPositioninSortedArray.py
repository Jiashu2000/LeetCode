# 34. Find First and Last Position of Element in Sorted Array

from typing import List



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)

        if left == len(nums) - 1 or nums[left + 1] != target:
            return [-1, -1]
        if right == 0 or nums[right - 1] != target:
            return [-1, -1]
        
        return [left + 1 , right - 1]
        
    
    # find the rightmost element that is smaller than the target
    def searchLeft(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            print("left", left)
            print("right", right)
            mid = left + (right - left)//2
            print("mid", mid)
            print('-----')
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return right
    
    # find the leftmost element that is larger than the target
    def searchRight(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left)//2
            print("left", left)
            print("right", right)
            print("mid", mid)
            print('---')
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


solution = Solution()
arr = [5, 7 , 7, 8, 8, 10]
target = 6

arr1 = []
target1 = 0

print(solution.searchRange(arr1, target1))


''' 
time complexity: o(logn)
space complexity: o(1)
'''
