# [Two Sum](https://leetcode.com/problems/two-sum/)

Level: <code style="color: green">Easy</code>

Given an array of integers `nums` and an integer `target`, return _indices_ of the two numbers such that they add up to `target`. You may assume that each input would have __exactly one solution__, and you may not use the same element twice. You can return the answer in any order.

__Example 1__:
> __Input:__ nums = [2,7,11,15], target = 9</br>
> __Output__: [0,1]</br>
> __Explanation__: Because nums[0] + nums[1] == 9, we return [0, 1].

__Example 2__:
> __Input__: nums = [3,2,4], target = 6</br>
> __Output__: [1,2]

__Example 3__:
> __Input__: nums = [3,3], target = 6</br>
> __Output__: [0,1]

__Constraints__:
- 2 <= nums.length <= 10<sup>4</sup>
- -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>
- -10<sup>9</sup> <= target <= 10<sup>9</sup>
- __Only one valid answer exists.__

__Follow-up__: Can you come up with an algorithm that is less than O(n<sup>2</sup>) time complexity?

***
## My Solution

### Explanation
Things to keep in mind:
- there is only one solution in given input, meaning the moment we find two numbers whose sum is equal to target, we can return. We don't have to move any further in the list.
- we can not use the same element twice to get the sum as target.

Since one of the asks is to reduce time complexity from O(n<sup>2</sup>), we should avoid nested looping. We can achieve this by storing already seen items in the list into a dictionary with index of that item as the value. That way we can quickly get number's index from list, in case we needed it later.

```python
    def twoSum(nums: List[int], target: int) -> List[int]:
        t1 = dict()

        for idx, num in enumerate(nums):
            if (target - num) in t1:
                return [t1[target - num], idx]
            t1[num] = idx
        return []
```

## Best Solution by Memory from Leetcode:
A solution that does really well Memory wise is:
```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, ele1 in enumerate(nums):
            for index2, ele2 in enumerate(nums, start=0):
               if ele1 + ele2 == target and index1 != index2:
                   return [index1,index2]
```
