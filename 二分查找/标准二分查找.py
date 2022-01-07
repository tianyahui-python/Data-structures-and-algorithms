"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1

        while last >= first:
            # 以下写法等同于 (first+last) // 2
            # 为什么用下面的写法，因为防止整数越界，当first和last 都是非常大的数字的时候，相加的和就会导致超出整数的范围，导致整数越界
            mid = first + (last-first) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                last = mid - 1
            else:
                first = mid + 1

        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    Solution.search(nums, target)
