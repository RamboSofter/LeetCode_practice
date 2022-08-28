"""
201. 数字范围按位与
https://leetcode.cn/problems/bitwise-and-of-numbers-range/
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return right << shift
