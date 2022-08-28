"""
540. 有序数组中的单一元素
https://leetcode.cn/problems/single-element-in-a-sorted-array/
"""
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """二分查找"""
        n = len(nums)
        if n == 1:
            return nums[0]

        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2
            if mid < n - 1 and nums[mid] not in [nums[mid - 1], nums[mid + 1]]:
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid

        return nums[left]
