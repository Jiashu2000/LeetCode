# Day 1 
# October 11

'''
数组理论基础
- 数组是存放在连续内存空间上的相同类型数据的集合

- 数据下标都是从0开始的
- 数组内存空间的地址都是连续的


'''

# Question 704. Binary Search

class Solution:

    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    


    def search2(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return - 1


arr = [-1, 0, 2, 5, 9, 12]
target = 9 

solution = Solution()
print(solution.search2(arr, target))


'''
清楚区间定义
区间定义就是不变量


二分法的两种写法

1. 左闭右闭 [left, right]

定义target在[left, right]:
    - while (left <= right) 要使用 <=, 因为left == right是有意义的。
    - if (nums[middle] > right), right要赋值middle - 1. 因为当这个nums[middle]一定不是target,
    那么接下来要查找的左区间结束的下标位置就是middle - 1

time complexity: o(logn)
space complexity: o(1)


2. 左闭右开 [left, right)

定义target在[left, right):
    - while (left < right), 这里使用<, 因为left == right在区间[left, right)是没有意义的
    - if (nums[middle] > target) right更新为middle. 因为当前nums[middle]不等于target, 去左区间继续寻找
    因为寻找的区间是左闭右开, 所以right更新为middle.

time complexity: o(logn)
space complexity: o(1)

'''