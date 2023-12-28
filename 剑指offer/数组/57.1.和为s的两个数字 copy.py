# 一定有解，不考虑无解情况
# 双指针
class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        left = 0
        right = len(price)-1
        while right>=left:
            if price[left]+price[right]>target:
                right-=1
            elif price[left]+price[right]<target:
                left+=1
            else:
                return [price[left],price[right]]