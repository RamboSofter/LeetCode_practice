"""
45. 跳跃游戏 II
https://leetcode.cn/problems/jump-game-ii/
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jump_max = 0
        jump_min = 0
        res = 0
        cur = 0
        while jump_min < n:
            jump_min = jump_max + 1
            jump_max = nums[cur] + cur

            if jump_max >= n - 1:
                return res + 1

            temp_max = 0
            for i in range(jump_min, jump_max + 1):
                if i + nums[i] > temp_max:
                    temp_max = i + nums[i]
                    cur = i
            res += 1

        return res
