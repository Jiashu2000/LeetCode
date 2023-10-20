# 18. 4Sum 


from typing import List

# 双指针法
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            a = nums[i]
            # a 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                # b 去重
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                b = nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    tot = a + b + nums[left] + nums[right]
                    if tot > target:
                        right -= 1
                    elif tot < target:
                        left += 1
                    else:
                        res.append([a, b, nums[left], nums[right]])
                        while left + 1 < right and nums[left] == nums[left +1]:
                            left += 1
                        while right - 1 > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res 

'''
time complexity: o(n^3)
space complexity:: o(1)
'''