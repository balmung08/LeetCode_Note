#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
# 常规二维DP
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[-1])
        note = [[0 for i in range(m)] for j in range(n)]
        note[0][0] = triangle[0][0]
        for i in range(1,m):
            for j in range(i+1):
                if j == 0:
                    note[i][j] = note[i-1][0]+triangle[i][j]
                elif j == i:
                    note[i][j] = note[i-1][i-1]+triangle[i][j]
                else:
                    note[i][j] = min(note[i-1][j],note[i-1][j-1])+triangle[i][j]
        return min(note[-1])   

# 实际上每一行仅与上一行相关，因此两个一维数组/二列的二维数组就足够迭代
# 优化如下：
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(2)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            curr, prev = i % 2, 1 - i % 2
            f[curr][0] = f[prev][0] + triangle[i][0]
            for j in range(1, i):
                f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
            f[curr][i] = f[prev][i - 1] + triangle[i][i]
        return min(f[(n - 1) % 2])

# 实际上一个一维数组就可以完成
# 必须要递减的迭代
# 要使用的点在当前迭代点左边
# 递减迭代可以使得迭代点右边是已经更新的数据，左边仍为上一行的
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]
        
        return min(f)
# @lc code=end

