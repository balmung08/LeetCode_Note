#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
# 走过的位置不用新列表来标记了，直接把内容改了
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] == "0"
                    # 开始BFS
                    List = [[i,j]]
                    while List:
                        x,y = List.pop(0)
                        for new_x, new_y in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0' 
                                List.append([new_x, new_y])
        return count
        
        
# @lc code=end

