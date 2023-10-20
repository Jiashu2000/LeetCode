# LCR 182. 动态口令

class Solution:

    def dynamicPassword(self, password: str, target: int) -> str:
        return password[target: ] + password[:target]
    
    # 局部反转+整体反转
    def dynamicPassword2(self, password: str, target: int) -> str:
        password = list(password)
        password = password[::-1]
        prev = len(password) - target
        password[:prev] = password[:prev][::-1]
        password[prev:] = password[prev:][::-1]
        return ''.join(password)
    
    '''
    time complexity: o(n)
    space complexity: o(n)    
    '''