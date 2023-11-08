#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
'''
# 时间复杂度太高，直接超时了
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i in range (len(height)):
            for j in range (i+1,len(height)):
                v = min(height[i],height[j])*(j-i)
                if v>=max:
                    max = v
        return max
'''
# 双指针对冲问题
# 哪边边长小哪边移动
class Solution:
    def maxArea(self, height: List[int]) -> int:        
        head = 0
        max = 0
        tail = len(height)-1
        while tail>=head:
            V = min(height[head],height[tail])*(tail-head)
            if V>=max:
                max = V
            if height[head]>=height[tail]:
                tail -= 1
            else:
                head += 1
        return max

# @lc code=end

