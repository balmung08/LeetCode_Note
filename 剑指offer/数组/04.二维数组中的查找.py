# 暴力解本身没啥意义
# 找规律，从左下角开始，向上会变小，向右会变大
# 因此目前值小于目标值就向右，大于目标值就向左
class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        if not plants: return False
        m, n = len(plants), len(plants[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if plants[row][col] < target:
                col += 1
            elif plants[row][col] > target:
                row -= 1
            else:
                return True
        return False
'''
# 对角线二分查找
# 对于每一个对角线所在的行和列都进行二分查找
# 无论是不是正方形都可以完成所有元素的遍历
# 实际上并不比找规律分治要快，且代码也不方便维护
class Solution:
    def binary_search(self, plants, target, start, vertical):
        lo = start
        hi = len(plants) - 1 if vertical else len(plants[0]) - 1 # 垂直搜索：hi = 行数 - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical:  # 垂直搜索
                if plants[mid][start] < target:
                    lo = mid + 1
                elif plants[mid][start] > target:
                    hi = mid - 1
                else: 
                    return True
            else:   # 水平搜索
                if plants[start][mid] < target:
                    lo = mid + 1
                elif plants[start][mid] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        if not plants: return False   # 边界条件

        for i in range(min(len(plants), len(plants[0]))):
            vertical_found = self.binary_search(plants, target, i, True) # 垂直方向是否找到
            horizontal_found = self.binary_search(plants, target, i, False) # 水平是否找到
            if vertical_found or horizontal_found:  # 任一方向找到即可
                return True

        return False
'''