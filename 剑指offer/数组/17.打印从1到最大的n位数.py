class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        end = 10**cnt
        res = []
        for i in range(1,end):
            res.append(i)
        return res