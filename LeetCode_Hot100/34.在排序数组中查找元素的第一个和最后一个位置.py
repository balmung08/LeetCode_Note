#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
'''
# 先写个复杂度为n的遍历试试看
# 能通过，但是毕竟不符合题目的logn要求
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L = len(nums)
        res = []
        for i in range(0,L):
            if nums[i] == target:
                res.append(i)
                try:
                    while nums[i] == target:
                        i += 1
                    res.append(i-1)
                except IndexError as e:
                    pass
                    res.append(i-1)
                return res
        return [-1,-1]
'''
'''
# 一次二分+区间扩散
# 在极端情况，如所有数据相同时会从logn退化为n
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = 0 
        L = last = len(nums) - 1  
        found = False 
        while first <= last and not found:  
            midpoint = (first + last) // 2 
            if nums[midpoint] == target:  
                found = True 
                position = midpoint
            else: 
                if target < nums[midpoint]: 
                    last = midpoint - 1  
                else: 
                    first = midpoint + 1 
        if found == False:
            return [-1,-1]
        # 先二分查找数字，然后往前后扩散
        pos_L = pos_R= position
        print(position)
        while pos_L>=0 and nums[pos_L] == target :
            pos_L -= 1
        while  pos_R<=L and nums[pos_R] == target:
            pos_R += 1
        return [pos_L+1,pos_R-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        # 第一次二分查找，确定左边界
        # 常规的二分法找到就停，但是如果一直不停可以找到边界
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]==target:
                right=mid
            else:
                right=mid-1

        if nums[left]!=target:
            return [-1,-1]
        
        # 已知左边界，从左边界开始向右找右边界
        l2=left
        r2=len(nums)-1
        while l2<=r2:
            m2=(l2+r2)//2
            if nums[m2]==target:
                l2=m2+1
            elif nums[m2]>target:
                r2=m2-1
        return [left,l2-1]
# @lc code=end

