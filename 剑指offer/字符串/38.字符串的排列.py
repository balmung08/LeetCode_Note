# 和全排列思路一模一样
# 在最后额外加一个set用于去重即可
class Solution:
    def __init__(self) -> None:
        self.res = []
        self.hmap = set()
    def goodsOrder(self, goods: str) -> List[str]:
        path = ""
        def dfs(n,path):
            if n == len(goods):
                if not (path in self.hmap):
                    self.res.append(path)
                    self.hmap.add(path)
                return None
            else:
                for i in range(0,len(path)+1):
                    dfs(n+1,path[:i]+goods[n]+path[i:])
        dfs(0,path)
        return self.res