#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
'''
# 好好好，直接遍历果然又超时了
# 那试着用字典存一下数据再读，减少复杂度为2n
# 但是使用了额外的存储空间
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = []
        d = {}
        for i in nums:
            d[i] = True
        for i in range(1,len(nums)+1):
            if not d.get(i):
                r.append(i)
                
        return r
'''
'''
# 特殊思路：在原表上进行修改
# 把每个i对应的nums[i]改成负数，最后哪几个nums[n]是正的，n就没出现过
# 好奇怪的思路，但是很有意思
# 这个操作多进行了一次比较反而减慢了速度，但是不使用额外的空间
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        r = []
        for i in nums:
            # 注意，之前前面的操作可能导致某一位变成负数
            # 负数要进行这个操作要取绝对值
            if nums[abs(i)-1]>0:
                nums[abs(i)-1] *= -1
        for i in range(0,len(nums)):
            if nums[i]>0:
                r.append(i+1)
        return r
'''
# 要想极致速度得用集合
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans =[]
        # 用list的元素创建一个无序不重复集合，重复的被删除
        # set和dict类似，操作复杂度基本上都是1
        # 这里set操作转换遍历一次list，插入set，一共是n+1
        # set函数比自己遍历再加入字典要快，上面那个方法是2n
        a = set(nums)
        for i in range(1,len(nums)+1):
            if i not in a:
                ans.append(i)
        return ans

# @lc code=end

