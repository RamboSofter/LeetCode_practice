"""
213. 打家劫舍 II
https://leetcode.cn/problems/house-robber-ii/
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def my_rob(nums: List[int]):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[1:]), my_rob(nums[:n - 1]))
