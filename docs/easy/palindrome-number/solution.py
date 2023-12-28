class MySolution:
    @staticmethod
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


class FastestRuntimeSolution:
    # https://leetcode.com/problems/palindrome-number/submissions/1127926119/
    # ask to not convert string was a follow-up, and not the main requirement
    @staticmethod
    def isPalindrome(x: int) -> bool:
        x = str(x)
        return x[::-1] == x


class FastestRuntimeWithFollowUpSolution:
    # https://leetcode.com/problems/palindrome-number/submissions/1127926119/
    @staticmethod
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


class BestMemorySolution:
    # https://leetcode.com/problems/palindrome-number/submissions/1127926119/
    @staticmethod
    def isPalindrome(x: int) -> bool:
        s = str(x)
        rev_s = s[::-1]

        return True if s == rev_s else False


s = MySolution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
print(s.isPalindrome(11))