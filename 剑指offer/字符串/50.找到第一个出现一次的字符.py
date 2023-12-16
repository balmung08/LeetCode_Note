'''
# 从原理上时间复杂度最少就是O(n)
# 使用多维列表计数后排序，获取第一个一次数
# 复杂度很高
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        rem = [[-1 for i in range(3)] for j in range(26)]
        alphabet= [chr(i) for i in range(ord('a'), ord('z')+1)]
        for i in range(26):
            rem[i][2] = i
        for i in range(0,len(arr)):
            if rem[ord(arr[i])-ord('a')][0] != -1:
                rem[ord(arr[i])-ord('a')][1]+=1
            else:
               rem[ord(arr[i])-ord('a')][0] = i  
               rem[ord(arr[i])-ord('a')][1] = 1
        res = list(n for n in rem if n[1]==1)
        if res == []:
            return " "
        res.sort()
        return alphabet[res[0][2]]
'''
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        rem = {}
        for i in arr:
            if i in rem:
                rem[i] = 0
            else:
                rem[i] = 1
        for key,value in rem.items():
            if value:
                return key 
        return " "