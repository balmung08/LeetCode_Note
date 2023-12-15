#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
'''
# 三种情况直接返回
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = [0]*26
        for i in tasks:
            hashmap[ord(i)-ord('A')]+=1
        hashmap = sorted(hashmap)
        # AXX AXX A
        # ABX ABX AB
        # ABCD ABC AB 这种时候没有空位，直接返回tasks长度
        minlen = (n+1)*(hashmap[25]-1) + 1 
        for i in hashmap[:-1]:
            if i == hashmap[-1]:
                minlen += 1
        return max(minlen,len(tasks))
'''
# 优先队列解法： 定义两个优先队列que1和que2
# que1是现在可以执行的任务，que2是需要等待的任务
# que1按任务的数量排序，que2按等待的时长排序
# 每个单位时间，从que1中弹出数量最多的任务完成，如果数量大于1，
# 则将下次执行的最短时间和数量-1放进que2中
# 之后将que2中冷却好的任务放进que1里。
# 如果que1为空，则等待到que2里面最快的任务完成
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        que1=[-count for count in Counter(tasks).values()]  #可执行的任务
        que2=[]#等待中的任务
        heapify(que1)
        cur_time=0
        while que1 or que2:
            if que1:
                count=heappop(que1)
                cur_time+=1
                if count+1:
                    heappush(que2,(cur_time+n,count+1))
            else:
                cur_time=que2[0][0]
            while que2 and que2[0][0]<=cur_time:
                heappush(que1,heappop(que2)[1])
        return cur_time
# @lc code=end
