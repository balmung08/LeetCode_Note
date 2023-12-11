#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
# 找出所有可能的路径并判断
# 也可以不使用额外的空间来记录是否经过，而是在原本的board上进行修改
class Solution:
    def __init__(self) -> None:
        self.res = False
    def exist(self, board: List[List[str]], word: str) -> bool:
        a = len(board)#行
        b = len(board[0])#列
        L = len(word)
        note = [[False for i in range(b)] for j in range(a)]
        def dfs(i,j,n):
            # print(i+1,j+1,n+1,note)
            if self.res or i>=a or j>=b or i<0 or j<0:
                return None
            if board[i][j]==word[n] and note[i][j] == False:
                note[i][j] = True
                if n == L-1:
                    self.res = True
                    return None 
                else:
                    dfs(i+1,j,n+1)
                    dfs(i,j+1,n+1)
                    dfs(i-1,j,n+1)
                    dfs(i,j-1,n+1)
                    note[i][j] = False
   
        for i in range(a):
            for j in range(b):
                if board[i][j] == word[0]:
                    
                    dfs(i,j,0)
                    if self.res:
                        return True
        return False
# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]\n"ABCESEEEFS"\n
# @lc code=end

