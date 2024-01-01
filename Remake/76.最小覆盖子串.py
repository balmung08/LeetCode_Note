#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def getIdx(x):
            return ord(x) - ord('A') + 26 if 'A' <= x <= 'Z' else ord(x) - ord('a')
        c1, c2 = [0] * 60, [0] * 60
        num = 0
        for i in t:
            c2[getIdx(i)]+=1
            if c2[getIdx(i)]==1:
                num += 1
        left = 0
        m = 100001
        ans = ""
        for right in range(0,len(s)):
            idx1 = getIdx(s[right])
            c1[idx1] += 1
            if c1[idx1]==c2[idx1]:
                num -= 1
            while left<right: 
                idx2 = getIdx(s[left])
                if c1[idx2]>c2[idx2]:
                    c1[idx2]-=1
                    left+=1
                else:
                    break
            if num == 0 and (right-left)<=m:
                m = right-left
                ans = s[left:right+1]
        return ans
'''
# 将列表换为字典
# 思路一模一样但是变快了
# 注意defaultdict的作用：给不存在的key一个默认值，不会出现keyerror
class Solution:    
    def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果

# @lc code=end
        
