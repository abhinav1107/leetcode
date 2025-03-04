# [](https://leetcode.com/problems/two-sum/)

Given an array of integers, calculate the ratios of its elements that are **positive**, **negative** and **zero**. Print the decimal value of each fraction on a new line with 6 places after the decimal.

__Example 1__:
> __Input__: arr = [1, 1, 0, -1, -1]</br>
> __Output__:
> ```text
> 0.400000
> 0.400000
> 0.200000
> ```
> __Explanation__: there are n = 5 elements: 2 positive, 2 negative and 1 zero. Their ratios are 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000.

***
## My Solution

```python
#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = len(arr)
    if count == 0:
        print(format(0, '.6f'))
        print(format(0, '.6f'))
        print(format(0, '.6f'))
        return
    n = 0
    p = 0
    z = 0
    ratio_arr = [0.000000, 0.00000, 0.000000]

    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1

    print(format((ratio_arr[0] + (p/count)), '.6f'))
    print(format((ratio_arr[0] + (n/count)), '.6f'))
    print(format((ratio_arr[0] + (z/count)), '.6f'))
    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
```
