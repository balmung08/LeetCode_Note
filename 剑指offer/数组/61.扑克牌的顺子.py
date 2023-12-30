'''
# 先确定0的个数，再分析情况
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        places.sort()
        num = list(n for n in places if n!=0)
        for i in range(len(places)):
            if places[i] == places[i-1] and places[i] != 0:
                return False
        delta = num[-1]-num[0]
        ifdelta<5:
            return True
        return False
'''
# 获取0个数的方式可简化
class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        unknown = 0
        places.sort() 
        for i in range(4):
            if places[i] == 0: unknown += 1 
            elif places[i] == places[i + 1]: 
                return False 
        return places[4] - places[unknown] < 5 

# 也可以使用哈希表遍历进行确认