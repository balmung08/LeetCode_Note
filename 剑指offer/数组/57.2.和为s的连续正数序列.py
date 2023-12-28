'''
# 双循环遍历
# 能过但是时间很慢
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        left = 1
        right = 2
        res = []
        tmp = []
        while left<=target//2:
            right = left+1
            while (left+right)/2*(right-left+1)<=target:
                if (left+right)/2*(right-left+1)==target:
                    tmp = list(range(left,right+1))
                    res.append(tmp)
                right+=1
            left+=1
        return res
'''
# 双指针标定位置
# 有提升但是还是比较慢
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        left = 1
        right = 2
        res = []
        while left<=target//2:
            if (left+right)/2*(right-left+1)<target:
                right += 1
            if (left+right)/2*(right-left+1)>target:
                left += 1
            if (left+right)/2*(right-left+1)==target:
                res.append(list(range(left,right+1)))
                left += 1
        return res

# 把求和公式改为加法
# 注意指针变化和s变化的顺序
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        left = 1
        right = 2
        s = 3
        res = []
        while left<=target//2:
            if s<target:
                right += 1
                s += right
            elif s>target:
                s -= left
                left += 1
            elif s==target:
                res.append(list(range(left,right+1)))
                s -= left
                left += 1
        return res

# 还可以根据求和公式，知道左界解右界并验证右界是否是整数
# 但是实测比上面双指针慢一点
class Solution:
    def fileCombination(self, target: int):
        i, j, res = 1, 2, []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res
