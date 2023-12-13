# 可精简的方向:把notes二维数组使用集合来记录，可以减少使用空间
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def __init__(self):
        self.res = 0
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        note = [[False for i in range(n)] for j in range(m)]
        def dfs(i,j):
            if i>=m or j>=n or note[i][j]:
                return None
            if digitsum(i)+digitsum(j)<=cnt:
                note[i][j] = True
                self.res += 1
                dfs(i+1,j)
                dfs(i,j+1)
        dfs(0,0)
        return self.res
