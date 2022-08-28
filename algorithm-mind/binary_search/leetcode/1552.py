"""
1552. 两球之间的磁力
https://leetcode.cn/problems/magnetic-force-between-two-balls/
"""

from typing import List


class Solution:
    def can_put_balls(self, pos: List[int], distance: int) -> int:
        pre = pos[0]
        cnt = 1
        for p in pos[1:]:
            if p - pre >= distance:
                cnt += 1
                pre = p
        return cnt

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        left = 1
        right = position[-1]

        while left < right:
            mid = (left + right + 1) // 2
            if self.can_put_balls(position, mid) >= m:
                left = mid
            else:
                right = mid - 1

        return left
