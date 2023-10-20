# 59. SpiralMatrixII

from typing import List

'''
坚持循环不变量的原则

填充上行从左到右
填充右列从上到下
填充下行从右到左
填充左列从下到上

保持每一条边左闭右开或者左开右闭

'''

class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for _ in range(n)]
        offset = 0
        count = 1
        startx = 0
        starty = 0
        while count < n**2 +1:
            for i in range(starty, n - offset):
                matrix[startx][i] = count
                count += 1
            for j in range(startx + 1, n - offset):
                matrix[j][n - offset - 1] = count
                count += 1
            for i in range(n - offset - 2, starty - 1, -1):
                matrix[n - offset - 1][i] = count
                count += 1
            for j in range(n - offset - 2, startx, -1):
                matrix[j][startx] = count
                count += 1
            startx += 1
            starty += 1
            offset += 1
        return matrix


    '''
    time complexity: o(n^2)
    space complexity: o(1)
    '''


    def generateMatrixExample(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0           # 起始点
        loop, mid = n//2, n//2          # 迭代次数, n为奇数时，矩阵的中心点
        count = 1                       # 计数

        for offset in range(1, loop+1):     # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset): # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset): # 从上至下
                nums[i][n-offset] = count
                count += 1
            for i in range(n - offset, starty, -1): # 从右至左
                nums[n-offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1): # 从下至上
                nums[i][starty] = count
                count += 1
        startx += 1     # 更新起始点
        starty += 1

        if n%2 != 0:    # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums