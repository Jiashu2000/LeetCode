# 406. Queue Reconstruction by Height


from typing import List

class Solution:
    '''
    understand how to use list!
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda a : (-a[0], a[1]))
        n = len(people)
        arr = list()
        for i in range(n):
            p = people[i]
            arr.insert(p[1], p)
        return arr
        
            
    def reconstructQueue_v1(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda a : (a[0], a[1]))
        n = len(people)
        arr = [-1] * n
        for i in range(n):
            p = people[i][0]
            front = people[i][1]
            j = 0
            while front > 0 or arr[j] != -1:
                if arr[j] != -1 and arr[j][0] < p:
                    j += 1
                    continue
                else:
                    j += 1
                    front -= 1
            arr[j] = people[i]

        return arr
        