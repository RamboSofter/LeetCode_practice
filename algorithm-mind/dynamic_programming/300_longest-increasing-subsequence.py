"""
300. 最长递增子序列
https://leetcode.cn/problems/longest-increasing-subsequence/
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        res = 0

        for num in nums:
            left = 0
            right = res
            while left < right:
                m = (left + right) // 2
                if tails[m] < num:
                    left = m + 1
                else:
                    right = m
            tails[left] = num
            if right == res:
                res += 1

        return res
