"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。


示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # records = dict()

        # 用枚举更方便，就不需要通过索引再去取当前位置的值
        # for idx, val in enumerate(nums):
        #     if target - val not in records:
        #         records[val] = idx
        #     else:
        #         return [records[target - val], idx] # 如果存在就返回字典记录索引和当前索引

        # 常规思路 暴力破解
        # 时间复杂度为O(n^2)
        # 空间复杂度为O(1)
        i = 0
        j = 1

        length = len(nums)
        while True:
            if j < length:
                if i <= (length-1):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    else:
                        j += 1
                else:
                    return
            else:
                i += 1
                j = i + 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1]

