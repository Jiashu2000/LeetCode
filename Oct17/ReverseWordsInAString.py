# 151. Reverse Words in a String

class Solution:

    def reverseWords(self, s: str) -> str: 
        list = s.split(" ")
        left = 0
        right = len(list) - 1
        while left < right:
            while left < right and list[left] == " ":
                left += 1
            while left < right and list[right] == " ":
                right -= 1
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        res = ""
        for i in list:
            if i != "":
                res = res + " " + i
        return res[1:]
    
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''

    def reverse_eg1(self, s: str) -> str:
        list = s.split()
        left = 0
        right = len(list) - 1
        while left < right:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        return ' '.join(list)
    
    '''
    str.split(sep = None)
    if sep is not specified or is None, runs of consecutive whitespace are regarded as a single separator,
    and the result will contain no empty strings at the starr or end if the string has 
    leading or trailing whitespace.
    '''


    def reverse_eg2(self, s: str) -> str:
        # 删除前后空白
        s = s.strip()
        # 翻转整个字符串
        s = s[::-1]
        # 将字符串拆分成单词，并反转每个单词
        s = ' '.join(word[::-1] for word in s.split())
        return s   