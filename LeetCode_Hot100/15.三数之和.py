#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
# 直接三重循环肯定要超时，二重循环加in查找实际上也是三重循环
# in查找操作也需要耗时，尽量别用=
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        #print(nums)
        for i in range(0,len(nums)):
            #print("i:",i)
            if nums[i] > 0:
                break
            head = i + 1
            tail = len(nums)-1
            while tail>head:
                #print("result:",nums[i]+nums[head]+nums[tail])
                if nums[i]+nums[head]+nums[tail]==0:
                    #print(i,head,tail)
                    if not ([nums[i],nums[head],nums[tail]] in out):
                        out.append([nums[i],nums[head],nums[tail]])
                        tail-=1
                        head+=1
                    else:
                        tail-=1
                        head+=1
                elif nums[i]+nums[head]+nums[tail]>0:
                    tail-=1
                elif nums[i]+nums[head]+nums[tail]<0:
                    head+=1
                #print(tail,head)
        return out
'''
'''
# 看见重复的连着两个数字直接跳过，就节省了查找是否重复的时间  
# s单独拉出来写，别每次判断都得算一次
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()
        #print(nums)
        for i in range(0,len(nums)-2):
            #print("i:",i)
            if nums[i] > 0:
                break
            head = i + 1
            tail = len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while tail>head:
                #print("result:",nums[i]+nums[head]+nums[tail])
                s = nums[i]+nums[head]+nums[tail]
                if s==0:
                    #print(i,head,tail)
                    out.append([nums[i],nums[head],nums[tail]])
                    tail-=1
                    head+=1
                    while nums[tail+1] == nums[tail] and tail>head:
                        tail -= 1
                    while nums[head-1] == nums[head] and tail>head:
                        head += 1
                elif s>0:
                    tail-=1
                elif s<0:
                    head+=1
                #print(tail,head)
        return out
'''
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0 or len(nums)<3:
            return []
        res = []
        for i in range(size):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            if nums[i] > 0:
                break
            l = i + 1
            r = size - 1
            while l < r:
                nl = nums[l]
                nr = nums[r]
                s = ni + nl + nr
                if s == 0:
                    res.append([ni,nl,nr])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res
'''
'''
# 达到最优性能需要使用字典
# 特殊避重思路1，不常规
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        ans = []
        for x in nums:
            d[x] = d.get(x,0)+1
        # 字典存的是数字和其出现次数
        a = [x for x in d if x > 0]#正数
        b = [x for x in d if x <= 0]#负数
        # 如果0出现大于两次，即三次就添加全0
        if d.get(0,0) > 2:
            ans.append([0,0,0])
        # 只有目标数在头尾之间时存到结果中，避免重复
        for pos_value in a:
            for neg_value in b:
                target = -(pos_value+neg_value)
                if target in d:
                    if target == pos_value and d[target] > 1:
                        ans.append([pos_value,pos_value,neg_value])
                    elif target == neg_value and d[target] > 1:
                        ans.append([pos_value,neg_value,neg_value])
                    elif target != pos_value and target != neg_value and pos_value >= target >= neg_value:
                        ans.append([pos_value,neg_value,target])
        return ans
'''
# 字典+二分查找法是最优思路，但是并不常规
# 特殊避重思路2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        counts={}
        for i in nums:
            counts[i]=counts.get(i,0)+1
        nums=sorted(counts)
        print(nums)
        for i,num in enumerate(nums):
            # 对出现了一次以上的数据进行处理
            if counts[num]>1:
                if num==0:
                    if counts[num]>2:
                        ans.append([0,0,0])
                        continue
                else:
                    if -num*2 in counts:
                        ans.append([num,num,-2*num])
            # 三个数都不相等时进行处理
            if num<0:
                two_sum=-num
                #二分查找剩余的两个数据 之和为 -num(正数)
                # left是表示从i+1开始，满足大于和减去最大数的第一个位置
                # 也就是可能成立的情况下两数里小数的最小值
                left=bisect.bisect_left(nums,(two_sum-nums[-1]),i+1)   
                # 右边界即表示小于和除以二的最大值
                # 也就是可能成立的情况下两数里小数的最大值
                for j in nums[left:bisect.bisect_right(nums,(two_sum//2),left)]:
                    k=two_sum-j
                    if k in counts and k!=j:
                        ans.append([num,j,k])
        return ans
# @lc code=end

