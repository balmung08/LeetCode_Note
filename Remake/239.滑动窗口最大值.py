#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
# 建倒序队列，用列表无法很方便的排出队头的元素
# 1234可以只保留4，因为4是最大值，123左出对max没有影响
# 但4321必须全部保留，因为4出完以后3就是最大值
# 如果5321进来一个3，则队列变为33，排除所有比要进来的数小的队列元素
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

#[1,3,1,2,0,5]\n3\n
# @lc code=end

