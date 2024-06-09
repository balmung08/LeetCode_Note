#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_orange = []
        bad_orange = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_orange.append((i,j))
                elif grid[i][j] == 2:
                    bad_orange.append((i,j))
        old_length = len(good_orange)
        count = 0
        # print(bad_orange)
        while True:
            old_length = len(good_orange)
            temp = []
            for i in bad_orange:
                if (i[0],i[1]+1) in good_orange:
                    if i[1]+1<len(grid[0]):
                        # print((i[0],i[1]+1))
                        good_orange.remove((i[0],i[1]+1))
                        temp.append((i[0],i[1]+1))
                if (i[0],i[1]-1) in good_orange:
                    if  i[1]-1>-1:
                        # print((i[0],i[1]-1))
                        good_orange.remove((i[0],i[1]-1))
                        temp.append((i[0],i[1]-1))
                if (i[0]+1,i[1]) in good_orange:
                    if i[0]+1<len(grid):
                        # print((i[0]+1,i[1]))
                        good_orange.remove((i[0]+1,i[1]))
                        temp.append((i[0]+1,i[1]))
                if (i[0]-1,i[1]) in good_orange:
                    if i[0]-1>-1:
                        # print((i[0]-1,i[1]))
                        good_orange.remove((i[0]-1,i[1]))
                        temp.append((i[0]-1,i[1]))
            if len(good_orange) == old_length:
                break
            count += 1
            bad_orange += temp
        # print("fin:",good_orange)
        if len(good_orange)==0:
            return count
        else:
            return -1
        

        
                

# @lc code=end

