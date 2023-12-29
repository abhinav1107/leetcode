from typing import List


class MySolution:
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        sorted_strs = sorted(strs, key=len)
        common_prefix = ""

        for i in range(len(sorted_strs[0])):
            for j in sorted_strs[1:]:
                if i == len(j) or sorted_strs[0][i] != j[i]:
                    return common_prefix
            common_prefix = common_prefix + sorted_strs[0][i]

        return common_prefix


class BestMemorySolution:
    # https://leetcode.com/problems/longest-common-prefix/submissions/1130926205/
    @staticmethod
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


m = MySolution()
print(m.longestCommonPrefix(["flower","flow","flight"]))
print(m.longestCommonPrefix(["dog","racecar","car"]))
m = BestMemorySolution()
print(m.longestCommonPrefix(["flower","flow","flight"]))
print(m.longestCommonPrefix(["dog","racecar","car"]))
