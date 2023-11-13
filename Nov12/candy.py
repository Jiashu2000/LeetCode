# 135. candy

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        arr = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                arr[i] = max(arr[i], arr[i-1] + 1)
        for j in range(n-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                arr[j] = max( arr[j], arr[j+1]+ 1)
        return sum(arr)