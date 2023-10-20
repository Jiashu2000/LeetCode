# 977. Squares of a Sorted Array

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        
        left_ptr = left - 1
        right_ptr = left

        while left_ptr >= 0 and right_ptr < n:
            
            left_nxt = nums[left_ptr] * nums[left_ptr]
            right_nxt = nums[right_ptr] * nums[right_ptr]
            if left_nxt < right_nxt:
                left_ptr -= 1
                res.append(left_nxt)
            else:
                right_ptr += 1
                res.append(right_nxt)
        
        while left_ptr >= 0:
            left_nxt = nums[left_ptr] * nums[left_ptr]
            left_ptr -= 1
            res.append(left_nxt)

        while right_ptr < n:
            right_nxt = nums[right_ptr] * nums[right_ptr]
            right_ptr += 1
            res.append(right_nxt)
        
        return res

    '''
    time complexity: o(n)
    space complexity: o(n)

    '''


    def twoPointers(self, nums : List[int]) -> List[int]:
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        res = [0] * len(nums)
        while l <= r:
            if nums[l]**2 < nums[r]**2:
                res[i] = nums[r]**2
                r -= 1
            else:
                res[i] = nums[l]**2
                l += 1
            i -= 1
        return res


    '''
    time complexity: o(n)
    space complexity: o(n)

    '''