# 27. Remove Element

from typing import List

class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        right = n - 1
        left = 0
        while left <= right:
            while right > left and nums[right] == val:
                right -= 1
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
            left += 1
        return right + 1
    

    '''
    time complexity: o(n)
    space complexity: o(1)

    '''
    

    def bruteforce(self, nums: List[int], val: int) -> int:
        i, l = 0, len(nums)
        while i < l:
            if nums[i] == val:
                for j in range(i+1, l):
                    nums[j-1] = nums[j]
                l -= 1
                i -= 1
            i += 1
        return l
            
          
    '''
    time complexity: o(n^2)
    space complexity: o(1)
    '''


    # 明确快慢指针的定义
    # 快指针：寻找新数组的元素，新数组就是不包含目标元素的数组
    # 慢指针：指向更新数组下标的位置
    def twopointers(self, nums: List[int], val: int) -> int:
        fast, slow = 0, 0
        n = len(nums)
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow 
    
    '''
    time complexity: o(n)
    space complecity: o(1)
    '''