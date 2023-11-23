#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# 直接遍历搜索确实能过，但是时间复杂度不符合
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index,value in enumerate(nums):
            if value == target:
                return index
        return -1
'''
# 二分查找，先处理升序，根据左右是否有序第一次二分找到转折点的位置
# 随后根据大小比较来在转折点的左/右边二分找目标值

# 也可以一边根据有序性查找转折点时，把有序的那边判断
# 如果有序的部分有目标则结束，没有则留下剩下部分，再找有序部分
# 其实复杂度是一样的，而且第一种程序上更容易实现一些
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums)-1
        turn = 0
        while head<tail:
            mid = (head+tail)//2
            print(head,tail,mid)
            if tail-head == 1:
                if nums[head]<nums[tail]:
                    turn = head
                    break
                else:
                    turn = tail
                    break
            if nums[mid]<nums[tail]:
                tail = mid
            else:
                head = mid
            turn = mid
        if nums[turn] == target:
            return turn
        elif nums[turn]>target:
            return -1
        else:
            if target == nums[-1]:
                return len(nums)-1
            elif target<nums[-1]:
                head = turn
                tail = len(nums)-1
                while head <= tail:
                    midpoint = (head + tail) // 2 
                    if nums[midpoint] == target:  
                        return midpoint
                    else: 
                        if target < nums[midpoint]: 
                            tail = midpoint - 1  
                        else: 
                            head = midpoint + 1 
                return -1
            else:
                head = 0
                tail = turn
                while head <= tail:
                    midpoint = (head + tail) // 2 
                    if nums[midpoint] == target:  
                        return midpoint
                    else: 
                        if target < nums[midpoint]: 
                            tail = midpoint - 1  
                        else: 
                            head = midpoint + 1 
                return -1

# @lc code=end

