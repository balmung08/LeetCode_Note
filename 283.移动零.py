#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
'''
# 头尾双指针向中间缩，两个指针分别代表未处理片段的头尾
# 每一个0处理一次
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        head = 0
        fin = tail = len(nums)
        while head<=tail and head<=fin-1:
            if nums[head] == 0:
                nums.pop(head)
                nums.append(0)
                tail -= 1
            else:
                head += 1
'''
# slow指向非0的末尾，fast指向待处理的头部
# 同时完成了删除0和往前移数字的要求
# 最后把最后几项赋成0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast = slow = 0
        fin =  len(nums)
        while fast<=fin-1:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(fast-slow):
            nums[slow+i]=0
'''
# 上面是赋值一次然后填充0
# 其实直接对换也可以，性能没啥差别，把非零放到前面
# 其实设个尾指针，把0放到尾部也是一样的
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
'''

'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    # 这个属实简洁，但是毕竟是n2，还是有点慢
    for i in range(nums.count(0)):
                nums.remove(0)
                nums.append(0)
'''
    

# @lc code=end

