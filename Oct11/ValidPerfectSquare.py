# 367. Valid Perfect Square

class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = left + (right - left)//2
            mid_pow = mid * mid
            if mid_pow == num:
                return True
            elif mid_pow > num:
                right = mid - 1
            else:
                left = mid + 1
        return False

