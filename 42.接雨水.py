#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
'''
# 每个柱子能接多少水由左右两边距离自己最近的最大项的和自己的高度三个要素决定
# 强行遍历结果对了，但是超时了，得想办法简化
class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        for i in range(0,len(height)):
            head = 0
            tail = len(height)-1
            max_l = 0
            max_r = 0
            while head<i:
                if max_l <= height[head]:
                    max_l = height[head]
                head += 1
            while tail>i:
                if max_r <= height[tail]:
                    max_r = height[tail]
                tail -= 1
            if min(max_l,max_r)>=height[i]:
                count += min(max_l,max_r)-height[i]
        return count    
'''
'''
# 可以把算出来的前后最大值存起来，然后算的时候读取
# 使用了三次遍历，时间上已经最优了，但使用了两个额外的空间
class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        head = 0
        n = len(height)
        l_m = [0]*n
        r_m = [0]*n
        max_l = max_r = 0
        for i in range(0,n):
            if max_l <= height[i]:
                max_l = height[i]
            l_m[i] = max_l
        for i in range(n-1,-1,-1):
            if max_r <= height[i]:
                max_r = height[i]
            r_m[i] = max_r
        for i in range(0,n):
            if min(l_m[i],r_m[i])>=height[i]:
                count += min(l_m[i],r_m[i])-height[i]
        return count  
'''

# 既然两侧由小的决定，那么哪边小哪边就往中间走一个刷新状态，大的不动
# 左右两侧交叉算
class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针
        if len(height) == 0:
            return 0
        max_l, max_r = 0, 0  # 初始化最长边
        res = 0
        i , j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                # 右边雨水能挡住左边雨水，去左边计算
                if height[i] < max_l:
                    res += (max_l - height[i])
                else:
                    max_l = height[i]
                i += 1
            else:
                # 去右边计算
                if height[j] < max_r:
                    res += (max_r - height[j])
                else:
                    max_r = height[j]
                j -= 1
        return res


# @lc code=end

