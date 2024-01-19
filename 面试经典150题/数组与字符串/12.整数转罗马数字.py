#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
# 贪心：每次使用最大的数字进行消去
class Solution:
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += hashmap[key] * count 
                num %= key
        return res

# 暴力分位数匹配
class Solution:
    def intToRoman(self, num: int) -> str:
        a,b,c,d= num//1000, num%1000//100, num%100//10, num%10
        ge  = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        shi = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        bai = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        qian =['','M','MM','MMM']
        str1 = ''
        str1 +=qian[a]+bai[b]+shi[c]+ge[d]
        return str1
# @lc code=end

