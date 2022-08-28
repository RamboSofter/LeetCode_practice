"""
593. 有效的正方形
https://leetcode.cn/problems/valid-square/
"""
from typing import List


class Solution:
    def __init__(self):
        self.len_t = -1

    def is_triangle(self, a: List[int], b: List[int], c: List[int]) -> int:
        l1 = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1])
        l2 = (a[0] - c[0]) * (a[0] - c[0]) + (a[1] - c[1]) * (a[1] - c[1])
        l3 = (b[0] - c[0]) * (b[0] - c[0]) + (b[1] - c[1]) * (b[1] - c[1])
        is_ok = (l1 == l2 and l1 + l2 == l3) or (l1 == l3 and l1 +
                                                 l3 == l2) or (l2 == l3 and l2 + l3 == l1)
        if not is_ok or l1 == l2 == l3:
            return False
        if self.len_t == -1:
            self.len_t = min(l1, l2)
        elif self.len_t != min(l1, l2):
            return False

        return True

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        return self.is_triangle(p1, p2, p3) and self.is_triangle(p1, p2, p4) and self.is_triangle(p2, p3, p4) and self.is_triangle(p1, p3, p4)
