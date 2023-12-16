# 维护一个双端队列
# 遇到重复的就把与其重复的前一项之前的所有项全部从左侧出队
# 双指针滑窗+哈希的方法也能实现这个原理
class Solution:
    def dismantlingAction(self, arr: str) -> int:
        l = len(arr)
        i, res = 0, 0
        queue = collections.deque()
        for i in arr:
            if i in queue:
                if len(queue) > res: res = len(queue)
                while queue.popleft() != i:
                    pass
            queue.append(i)
        if len(queue) > res: res = len(queue)
        return res
