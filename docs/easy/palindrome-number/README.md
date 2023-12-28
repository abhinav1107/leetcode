# [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Given an integer `x`, return `true` if `x` is a palindrome , and `false` otherwise.

> An integer is a palindrome when it reads the same forward and backward. For example, 121 is a palindrome while 123 is not.

__Example 1__:
> __Input__: x = 121</br>
> __Output__: true</br>
> __Explanation__: 121 reads as 121 from left to right and from right to left.

__Example 2__:
> __Input__: x = -121</br>
> __Output__: false</br>
> __Explanation__: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.

__Example 3__:
> __Input__: x = 10</br>
> __Output__: false</br>
> __Explanation__: Reads 01 from right to left. Therefore, it is not a palindrome.

__Constraints__:
- -2<sup>31</sup> <= x <= 2<sup>31</sup> - 1

__Follow up__: Could you solve it without converting the integer to a string?

***
## My Solution

### Explanation

Keep dividing number by 10 until the number becomes 0 and create an array with the remainder. Once done, check if reverse of array is same as the array.

A quick check would be every negative number is not-palindrome or any number between 0 and 9 is a palindrome.

```python
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        arr = []
        while x != 0:
            arr.append(x % 10)
            x = x // 10

        return arr == arr[::-1]
```

## Best Solution
```python
    def isPalindrome(x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        original_x = x

        while x > reversed_num:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return x == reversed_num or x == reversed_num // 10 if original_x >= 0 else False
```
### Explanation
Now that I have seen this solution, it does make sense.
- if the number is less than 0, then it can not be palindrome
- if the number is completely divisible by 10 and not 0, then it can not be a palindrome

Start by creating two numbers, one number which is copy of given number and other number which is 0. Then keep dividing the first number and adding the remainder to reverse number till first number is greater than reversed number. At the end, we would either be a number which is equal to reverse of first number or something that once divided by 10 once, will give the first number. This condition will depend on if the length of x is odd or even.

## Fastest solution
This is simple enough and doesn't require explanations.
```python
    def isPalindrome(x: int) -> bool:
        x = str(x)
        return x[::-1] == x
```
