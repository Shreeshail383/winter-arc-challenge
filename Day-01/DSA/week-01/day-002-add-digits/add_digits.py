
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num


if __name__ == "__main__":
    solution = Solution()
    print(solution.addDigits(38))   # 2
    print(solution.addDigits(0))    # 0
    print(solution.addDigits(123))  # 6
