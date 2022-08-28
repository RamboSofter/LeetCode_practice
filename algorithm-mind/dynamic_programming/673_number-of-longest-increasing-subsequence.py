"""
673. 最长递增子序列的个数
https://leetcode.cn/problems/number-of-longest-increasing-subsequence/
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        dp = [1 for i in range(n)]
        count = [1 for i in range(n)]

        max_count = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

                if dp[i] > max_count:
                    max_count = dp[i]
        res = 0
        for i in range(n):
            if max_count == dp[i]:
                res += count[i]

        return res
