#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start

# 双循环遍历会超时
# 用哈希表不满足存储空间的要求
# 把出现过的数4的nums[4]改成负数,最后看哪个数修改时已经是负数，但是修改了数组
'''
# 二分查找法
# 时间复杂度是nlogn
# 如果count严格大于mid,重复元素就在区间[left,mid]里；
# 否则，重复元素在区间[mid+1,right]
# 根据这个确认迭代的关系
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        # 这里指针很特殊，指的不是nums里的位置而是值的范围
        count = 0
        mid = 0
        while left<right :
            mid = (left + right) // 2
            count = 0
            # 重复值一定会导致理论中值的左右两边个数不一样多
            print(left,right,mid)
            for i in nums:
                if i<=mid:
                    count += 1
            if count<=mid:
                left = mid+1
            else:
                right = mid
        return left
'''
# 这个方法更是重量级
# 把数组类似于链表，每个位置是一个节点，位置内容是节点的next
# 用环形链表的思路，看在哪个节点快慢指针相遇，那个节点就是一个环
# 这里的环节点说明有两个或者多个节点指向一个节点，即多个槽里有同一个数字
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # 先找环节点
        while True:
            slow = nums[slow]           # 类比链表slow=slow.next
            fast = nums[nums[fast]]     # 类比链表fast=fast.next.next
            if fast == slow:    # 首次相遇点
                break
        # 设环前长度为n，环长为m
        # 此时相遇节点在环里走了m-n步，差n步回到起点节点
        # 让节点从起点开始，走n步，正好和原本节点一起到环起点
        fast = 0                # fast回到起点
        while slow != fast:     # 再次相遇点即为重复数字
            slow = nums[slow]
            fast = nums[fast]
        return fast
# @lc code=end

