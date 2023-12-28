'''
# 常规二分模板+特殊边界验证处理
class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        if records==[0]:
            return 1
        left=0
        right=len(records)-1
        while left<right:
            mid=(left+right)//2
            if records[mid]>mid:
                right=mid
            elif records[mid]==mid:
                left=mid+1
        if left == len(records)-1 and records[-1] == records[left-1]+1:
            return records[left]+1
        return records[left]-1
'''
# 二分时就把特殊情况处理掉
# 仔细考虑两个指针的关系就不用做特殊处理了
class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        i, j = 0, len(records) - 1
        while i <= j:
            m = (i + j) // 2
            if records[m] == m: 
                i = m + 1
            else: j = m - 1
        return i