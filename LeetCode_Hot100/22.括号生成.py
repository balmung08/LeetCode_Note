#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
    def generateParenthesis(self, n: int) -> List[str]:
        path = ""
        def dfs(left, right, path):
            if left == right and left==0:
                self.res.append(path)
                return None
            if left>0:
                dfs(left-1,right,path+"(")
            if right>left:
                dfs(left,right-1,path+")")
        dfs(n,n,path)
        return self.res
# @lc code=end

