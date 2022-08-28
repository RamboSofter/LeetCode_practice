"""
81. 搜索旋转排序数组 II
https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
"""

from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        left = 0
        right = n - 1

        while left < right and nums[right] == nums[0]:
            right -= 1
        if left == right:
            return nums[0] == target

        # 搜中间值
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] >= nums[0]:
                left = mid
            else:
                right = mid - 1
        idx = n
        if nums[right] >= nums[0] and right + 1 < n:
            idx = right + 1
        
        res = Solution.find(nums, 0, idx - 1, target)
        if res != -1:
            return True

        res = Solution.find(nums, idx, n - 1, target)

        return res != -1

    def find(nums: List[int], l: int, r: int, t: int) -> int:
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] >= t:
                r = mid
            else:
                l = mid + 1

        return r if nums[r] == t else -1
