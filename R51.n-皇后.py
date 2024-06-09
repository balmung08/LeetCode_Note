#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯法
        res = []
        s = '.' * n
        # path记录目前棋盘状态，i记录放了几个上去了
        # col那三个分别代表列、主对角线、次对角线
        # 由于是一行处理一次，行也不会放多个
        def backtrack(path=[], i=0, col_selected=[], z_diag=set(), f_diag=set()):
            if i == n:
                res.append(path)
                return 
            # J表示当前处理行的第J个位置
            for j in range(n):
                if j not in col_selected and i-j not in z_diag and i+j not in f_diag:
                    # |表示并集，实际上就是add
                    backtrack(path+[s[:j]+'Q'+s[j+1:]], i+1, col_selected+[j], z_diag|{i-j}, f_diag|{i+j})
            
        backtrack()
        return res


# @lc code=end

