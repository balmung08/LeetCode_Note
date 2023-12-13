# 与LC79完全相同
class Solution:
    def __init__(self):
        self.res = False
    def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
        p = len(grid)
        q = len(grid[0])
        note = [[False for i in range(q)] for j in range(p)]
        def dfs(i,j,n):
            if self.res or i<0 or j<0 or i>=p or j>=q or note[i][j]:
                return None
            if grid[i][j] == target[n]:
                if n == len(target)-1:
                    self.res = True
                    return None
                else:
                    note[i][j] = True
                    dfs(i+1,j,n+1)
                    dfs(i,j+1,n+1)
                    dfs(i-1,j,n+1)
                    dfs(i,j-1,n+1)
                    note[i][j] = False
        for i in range(p):
            for j in range(q):
                if grid[i][j] == target[0]:
                    dfs(i,j,0)
        return self.res