# [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string `""`.

__Example 1__:
> __Input__: strs = ["flower","flow","flight"]</br>
> __Output__: "fl"

__Example 2__:
> __Input__: strs = ["dog","racecar","car"]</br>
> __Output__: ""

__Constraints__:
- 1 <= `strs.length` <= 200
- 0 <= `strs[i].length` <= 200
- `strs[i]`, consists of only lowercase English letters.

***
## My Solution

### Explanation
I had to look at some of the discussion to understand that the word has to be a prefix. Earlier I understood that common part of all words can be any place.

For ex: `["care", "racecar", "scared"]` has `car` as the longest common word. This would have been definitely some more processing for sure.

Coming back to the problem, things to consider:
- the word is a prefix. The longest common word will be at the beginning of those words.
- the list will not be empty
- length of each word in the list is going to be anywhere from 0 to 200.
- longest common prefix can be equal to or smaller than the smallest word in the list.
- the simplest way to find common part would be to start a loop using index with first word in the list
  - keep matching the current character of the loop with corresponding characters in each word in the list
  - either we will cross length of the first word or we will find a mismatch.
  - keep appending to a placeholder string till we find match.
  - the moment we find a mismatch, we return with placeholder string

```python
    def longestCommonPrefix(strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=len)
        common_prefix = ""

        for i in range(len(sorted_strs[0])):
            for j in sorted_strs[1:]:
                if i == len(j) or sorted_strs[0][i] != j[i]:
                    return common_prefix
            common_prefix = common_prefix + sorted_strs[0][i]

        return common_prefix
```

Apparently this was the best runtime solution.

## Best Memory Solution
```python
    def longestCommonPrefix(strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for mot in strs:
            tempPrefix = ""
            for i in range(min(len(prefix), len(mot))):
                if prefix[i] == mot[i]:
                    tempPrefix += mot[i]
                else:
                    break
            prefix = tempPrefix

            if not prefix:
                break

        return prefix
```
