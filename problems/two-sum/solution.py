from typing import List


class Solution1:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        t1 = dict()

        for idx, num in enumerate(nums):
            if (target - num) in t1:
                return [t1[target - num], idx]
            t1[num] = idx
        return []


class Solution2:
    # top memory solution: https://leetcode.com/problems/two-sum/submissions/1127632510/
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i1, e1 in enumerate(nums):
            for i2, e2 in enumerate(nums, start=0):
                if e1 + e2 == target and i1 != i2:
                    return [i1, i2]
        return []


s = Solution1()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))

s = Solution2()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))