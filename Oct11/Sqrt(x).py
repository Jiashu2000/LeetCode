# 69. sqrt(x)


class Solution:
    
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left)//2
            mid_pow = mid * mid
            if mid_pow == x:
                return mid
            elif mid_pow > x:
                right = mid - 1
            else:
                left = mid + 1
        return right

'''
time complexity: o(logn)
space complexity: o(1)
'''