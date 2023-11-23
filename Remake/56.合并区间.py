#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
'''
# 最粗暴的依次合并递归方法超时了
# 这个方法的时间复杂度肯定是在n^2级别往上的，极端情况可能到高次方
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        flag = False
        for i in intervals:
            if result == []:
                result.append(i)
                continue
            for n in range(0,len(result)):
                # 在区间的左边
                if i[1]>=result[n][0] and i[1]<=result[n][1] and i[0]<=result[n][0]:
                    result[n] = [i[0],result[n][1]]
                    flag = True
                    break
                # 在区间的右边
                elif i[0]<=result[n][1] and i[0]>=result[n][0] and i[1]>=result[n][1]:
                    result[n] = [result[n][0],i[1]]
                    flag = True
                    break
                # 与区间重合
                elif i[0]>=result[n][0] and i[1]<=result[n][1]:
                    flag = True
                    break
                # 目前区间被覆盖
                elif i[0]<=result[n][0] and i[1]>=result[n][1]:
                    flag = True
                    result[n] = i
                    break
                if n == len(result)-1:
                    result.append(i)
        # 对result递归合并至没有可以合并的为止
        if flag == False:
            return result
        elif flag == True:
            return self.merge(result)
'''
# 如果首先对各个区间按左边界排序一次，可以省去很多条件判断
# 此时新区间一定在老区间的重合、覆盖于右边，条件可以极大简化
# 另外此时也可以保证区间的依次增长，一次循环完事而不需要再递归结果
# 时间复杂度是nlogn
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        res = []
        intervals.sort(key=lambda x: x[0]) 
        for inter in intervals:
            # 只需要管右边的条件即可
            if len(res) == 0 or res[-1][1] < inter[0]: 
                res.append(inter)
            else:  
                res[-1][1] = max(res[-1][1], inter[1])
        return res

# @lc code=end

