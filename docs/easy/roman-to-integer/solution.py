class MySolution:
    @staticmethod
    def romanToInt(s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        num = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                num = num - roman[s[i]]
            else:
                num = num + roman[s[i]]

        return num + roman[s[-1]]


class FastestRuntimeSolution:
    # https://leetcode.com/problems/roman-to-integer/submissions/1128080874/
    @staticmethod
    def romanToInt(s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_value = 0
        result = 0

        for char in s:
            curr_value = roman_dict[char]
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            prev_value = curr_value

        return result


class MemoryEfficientSolution:
    # https://leetcode.com/problems/roman-to-integer/submissions/1128080874/
    @staticmethod
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


m = MySolution()
print(m.romanToInt('III'))
print(m.romanToInt('LVIII'))
print(m.romanToInt('MCMXCIV'))
