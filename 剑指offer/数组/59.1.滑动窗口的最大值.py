# 与LC239完全相同
class Solution:
    def maxAltitude(self, heights: List[int], limit: int) -> List[int]:
        if not heights or limit == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(limit):
            while deque and deque[-1] < heights[i]:
                deque.pop()
            deque.append(heights[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(limit, len(heights)):
            if deque[0] == heights[i - limit]:
                deque.popleft()
            while deque and deque[-1] < heights[i]:
                deque.pop()
            deque.append(heights[i])
            res.append(deque[0])
        return res