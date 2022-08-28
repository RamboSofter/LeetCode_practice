"""
413. 等差数列划分
https://leetcode.cn/problems/arithmetic-slices/
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        diff = nums[1] - nums[0]
        acc_len = 0
        res = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == diff:
                acc_len += 1
            else:
                diff = nums[i] - nums[i - 1]
                acc_len = 0
            res += acc_len

        return res
