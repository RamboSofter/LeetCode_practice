"""
209. 长度最小的子数组
https://leetcode.cn/problems/minimum-size-subarray-sum/

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

"""
from typing import List

import bisect


class Solution:
    # 前缀和 + 二分
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        res = n + 1
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        if pre_sum[-1] < target:
            return 0

        for i in range(1, n + 1):
            tmp_tar = pre_sum[i] - target
            if tmp_tar < 0:
                continue
            left = 0
            right = i
            while left < right:
                mid = (left + right + 1) // 2
                if pre_sum[mid] <= tmp_tar:
                    left = mid
                else:
                    right = mid - 1

            if pre_sum[right] <= tmp_tar:
                res = min(res, i - right)

        return res if res <= n else 0
