#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = m-1
        n2 = n-1
        num = len(nums1)-1
        while n2>=0:
            if n1>=0 and nums1[n1]>nums2[n2]:
                nums1[num] = nums1[n1]
                num-=1
                n1-=1
            else: 
                nums1[num] = nums2[n2]
                num-=1
                n2-=1

# [2,0]\n1\n[1]\n1
# [1]\n1\n[]\n0
# [0]\n0\n[1]\n1
# @lc code=end

