"""
384. 打乱数组
https://leetcode.cn/problems/shuffle-an-array/


洗牌算法
"""
import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        self.temp = list(self.nums)
        n = len(self.nums)
        for i in range(n):
            idx = random.randint(i, n - 1)
            self.temp[i], self.temp[idx] = self.temp[idx], self.temp[i]
        return self.temp
