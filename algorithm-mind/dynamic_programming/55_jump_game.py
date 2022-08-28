"""
55. 跳跃游戏
https://leetcode.cn/problems/jump-game/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        jump_max = 0
        for i, num in enumerate(nums):
            if jump_max >= i and i + num > jump_max:
                jump_max = i + num

        return jump_max >= n - 1
