#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
        self.alphabet = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],
                         ["j","k","l"],["m","n","o"],["p","q","r","s"],
                         ["t","u","v"],["w","x","y","z"]]
    def letterCombinations(self, digits: str) -> List[str]:
        path = ''
        end = len(digits)
        if end == 0:
            return []
        def dfs(n,path):
            if n==end:
                self.res.append(path)
                return
            else:
                for i in self.alphabet[int(digits[n])]:
                    dfs(n+1,path+i)
        dfs(0,path)
        return self.res

# @lc code=end

