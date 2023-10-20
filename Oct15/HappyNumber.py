# 202. Happy Number

class Solution:

    def __init__(self):
        self.record = set()

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n in self.record:
            return False
        self.record.add(n)

        tot = 0
        while n > 0:
            digit = n%10 
            n = n//10
            tot += pow(digit, 2)

        if tot == 1:
            return True
        return self.isHappy(tot)
    
    '''
    time complexity: o(logn)
        the sum of square function has a time complexity of logn since it iterates through the digits of the number n,
        and the number of digits is proportional to the logarithmn of n in base 10.

    space complexity: o(logn)
    '''


    def isHappy_pointers(self, n: int) -> bool:
        slow = n
        fast = n
        while self.get_sum(fast) != 1 and self.get_sum(self.get_sum(fast)):
            slow = self.get_sum(slow)
            fast = self.get_sum(self.get_sum(fast))
            if slow == fast:
                return False
        return True
    
    def get_sum(self, n: int) -> int:
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r**2
        return  new_num
    
    '''
    time complexity: o(logn)
    space complexity: o(1)
    '''
        