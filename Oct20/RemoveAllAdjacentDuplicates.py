# 1047. Remove All Adjacent  Duplicates in String

class Solution:

    def removeDuplicates(self, s: str) -> str:
        l = []
        n = len(s)
        for i in range(n):
            cur = s[i]
            if len(l) > 0 and l[-1] == cur:
                l.pop()
            else:
                l.append(cur)
        return ''.join(l)

    '''
    time complexity: o(n)
    space complexity: o(n)


    递归的实现就是：每一次递归调用都会把函数的局部变量、参数值和返回地址等压入调用栈中
    在企业项目开发中，尽量不要使用递归！在项目比较大的时候，由于参数多，全局变量等等，
    使用递归很容易判断不充分return的条件，非常容易无限递归（或者递归层级过深
    '''

    # 使用双指针模拟栈
    def twoPointer(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(s)
        
        while fast < length:
            res[slow] = res[fast]

            if slow > 0 and res[slow] == res[slow -1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return ''.join(res[:slow])

    '''
    time complexity: o(n)
    space complexity: o(1)
    '''