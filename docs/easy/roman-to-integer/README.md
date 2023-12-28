# [Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

| Symbol | Value |
|:------:|:-----:|
|   I    |   1   |
|   V    |   5   |
|   X    |  10   |
|   L    |  50   |
|   C    |  100  |
|   D    |  500  |
|   M    | 1000  |

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:
- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

__Example 1__:
> __Input__: s = "III"</br>
> __Output__: 3</br>
> __Explanation__: III = 3.

__Example 2__:
> __Input__: s = "LVIII"</br>
> __Output__: 58</br>
> __Explanation__: L = 50, V= 5, III = 3.

__Example 3__:
> __Input__: s = "MCMXCIV"</br>
> __Output__: 1994</br>
> __Explanation__: M = 1000, CM = 900, XC = 90 and IV = 4.

__Constraints__:
- 1 <= s.length <= 15
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is __guaranteed__ that `s` is a valid roman numeral in the range `[1, 3999]`

***
## My Solution

### Explanation
The algorithm is pretty simple for the most part
- Start by creating a dictionary that stores numerical value of roman character, so that we can reference it during our run.
- loop over each character, find its value from the above-mentioned dictionary and keep adding them.

Just one case we need to address in above. What happens when the roman number is something like `IV` or `IX` or `XL`, etc.

The solution is actually very simple. If we find any character, whose value is less than next character's value in string, simply deduct the string value from the final sum. And since we are running our loop for length of the string - 1 times, we need to add the final character's value once the loop is over.

```python
    def romanToInt(s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        num = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                num = num - roman[s[i]]
            else:
                num = num + roman[s[i]]

        return num + roman[s[-1]]
```

## Fastest Runtime
```python
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        prev_value = 0
        result = 0

        for char in s:
            curr_value = roman_dict[char]
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value  # Subtract twice the previous value
            else:
                result += curr_value
            prev_value = curr_value

        return result
```

I am not particularly sure how is this faster, but if I had to guess, I would assume `for i in range(len(s) - 1)` is making my implementation slower.

## Best Memory
```python
    def romanToInt(s: str) -> int:
        amts = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        edges = { "I": {"V": 4, "X": 9}, "X": {"L": 40, "C": 90}, "C": {"D": 400, "M": 900}}

        tot = 0
        edge_amt = None
        for i, char in enumerate(s):
            if edge_amt:
                edge_amt = None
                continue

            edge_amt = edges.get(char, {}).get(s[i + 1]) if i < len(s) - 1 else None
            tot += edge_amt if edge_amt else amts.get(char)

        return tot
```
