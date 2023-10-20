# LCR 122. 路径加密

class Solution:

    def pathEncryption(self, path: str) -> str:
        s = list(path)
        for i in range(len(path)):
            if s[i] == '.':
                s[i] = " "
        return ''.join(s)

'''
time complexity: o(n)
space complexity: o(n)

字符串是不可变类型，需要将其转化成列表，空间复杂度不能为o(1)
'''