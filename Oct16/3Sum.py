# 15. 3Sum

from typing import List

# 双指针法比哈希更efficient

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # 去重a
            if i > 0 and nums[i] == nums[i-1]:
                continue
            '''
                错误去重a方法，将会漏掉-1,-1,2 这种情况
                if (nums[i] == nums[i + 1]) {
                    continue;
                }
            '''
            num = nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                tot = num + nums[left] + nums[right]
                if tot > 0:
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    # 去重b, c
                    while left + 1 < right and nums[left] == nums[left+1]:
                        left += 1
                    while right - 1 > left and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

'''
time complexity: o(n^2)
space complexity: o(1)
'''
                
