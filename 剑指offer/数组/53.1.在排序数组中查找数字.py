# 一次二分+区间扩散
# 在极端情况，如所有数据相同时会从logn退化为n
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        first = 0 
        L = last = len(scores) - 1  
        found = False 
        while first <= last and not found:  
            midpoint = (first + last) // 2 
            if scores[midpoint] == target:  
                found = True 
                position = midpoint
            else: 
                if target < scores[midpoint]: 
                    last = midpoint - 1  
                else: 
                    first = midpoint + 1 
        if found == False:
            return 0
        # 先二分查找数字，然后往前后扩散
        pos_L = pos_R= position
        print(position)
        while pos_L>=0 and scores[pos_L] == target :
            pos_L -= 1
        while  pos_R<=L and scores[pos_R] == target:
            pos_R += 1
        return pos_R-1-pos_L
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
'''