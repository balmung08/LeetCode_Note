#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
# 可以先处理较短位数再处理剩余位数
# 也可以先补0使位数相等，一次处理完成
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        tmp = 0
        tail_a = len(a)-1
        tail_b = len(b)-1

        while tail_a>=0 and tail_b>=0:
            s = int(a[tail_a])+int(b[tail_b])+tmp
            if s == 3:
                res.insert(0,"1")
                tmp = 1
            elif s == 2:
                res.insert(0,"0")
                tmp = 1
            elif s == 1:
                res.insert(0,"1")
                tmp = 0
            else: 
                res.insert(0,"0")
                tmp = 0
            tail_a-=1
            tail_b-=1
        if tail_a>=0:
            for i in range(len(a)-1,len(b)-1,-1):
                s = int(a[tail_a])+tmp
                if s == 3:
                    res.insert(0,"1")
                    tmp = 1
                elif s == 2:
                    res.insert(0,"0")
                    tmp = 1
                elif s == 1:
                    res.insert(0,"1")
                    tmp = 0
                else: 
                    res.insert(0,"0")
                    tmp = 0  
                tail_a-=1              
        elif tail_b>=0:
            for i in range(len(b)-1,len(a)-1,-1):
                s = int(b[tail_b])+tmp
                if s == 3:
                    res.insert(0,"1")
                    tmp = 1
                elif s == 2:
                    res.insert(0,"0")
                    tmp = 1
                elif s == 1:
                    res.insert(0,"1")
                    tmp = 0
                else: 
                    res.insert(0,"0")
                    tmp = 0   
                tail_b-=1

        if tmp == 1:
            res.insert(0,"1")
        return "".join(res)
# @lc code=end

