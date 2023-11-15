# 738. Monotone Increasing Digits

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n <= 0:
            return n 
        prev = None
        i = 1
        carry = 0
        digits = []
        idx = 0 
        borrowed_idx = -1

        while n > 0:
            cur = n%10 - carry
            carry = 0
            n = n//10
            if prev is None:
                prev = cur
            elif prev >= cur:
                digits.append(prev)
                prev = cur 
            elif prev < cur:
                borrowed_idx = idx
                if cur > 1:
                    digits.append(9)
                    prev = cur - 1
                    carry = 0
                else:
                    digits.append(9)
                    prev = 9
                    carry = 1
            idx += 1

        digits.append(prev)

        res = 0
        ten = 1

        for i in range(len(digits)):
            if i == len(digits) -1 and carry > 0:
                return pow(10, len(digits) -1) - 1
                break
            if i < borrowed_idx:
                res = res + 9 * ten
            else: 
                res = res + digits[i] * ten
            ten = ten * 10

        return res
                    
    def monotoneIncreasingDigits_eg(self, n: int) -> int:
        digits = list(str(n))
        last_borrow_idx = -1
        digits = [int(x) for x in digits]
        for i in range(len(digits) - 2, -1, -1):
            cur = digits[i]
            prev = digits[i+1]
            if cur <= prev:
                digits[i] = cur
                continue
            else:
                last_borrow_idx = i
                digits[i] = cur - 1
        num = 0
        i = 0

        if digits[0] <= 0:
            i = 1
        while i < len(digits):
            if last_borrow_idx != -1:
                if i <= last_borrow_idx:
                    num = num * 10 + digits[i]
                else:
                    num = num * 10 + 9
            else:
                num = num * 10 + digits[i]
            i += 1
        return num
    
    '''
    key is to find out the last index borrowed
    '''
                

            
            

