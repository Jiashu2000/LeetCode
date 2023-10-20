# 35. Search Insert Position

class Solution(object):

    def searchInsert(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            print("left", left)
            print("right", right)
            mid = left + (right - left)//2
            print("mid", mid)
            print("-----")
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


solution = Solution()

arr = [1,3,5,6]
target = 0
print(solution.searchInsert(arr, target))


'''
return left的原因:
right == left时候, 如果nums[mid] > target, left += 1. 如果nums[mid] < target, left保持不变
'''