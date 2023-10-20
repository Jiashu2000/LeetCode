# 349. Intersection of Two Arrays


from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for i in set2:
            if i in set1:
                res.append(i)
        return res

    '''
    time complexity: o(n)
    space complexity: o(n)
    '''


    def intersection_dict(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        return list(res)
    

    def intersection_array(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = [0] * 1001
        count2 = [0] * 1001
        result = []
        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        for j in range(len(nums2)):
            count2[nums2[j]] += 1
        for k in range(1001):
            if count1[k] * count2[k] > 0:
                result.append(k)
        return result

    def intersection_set(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

