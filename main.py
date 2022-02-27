class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """

        num = num[::-1]  # Reverse string of numbers
        for i in num:
            if int(i) % 2 == 1:  # If integer is odd, it is the leftmost odd integer
                print(num[num.index(i)::][::-1])
                return num[num.index(i)::][::-1]
        print("none")
        return ""


solution = Solution()

solution.largestOddNumber('52')

solution.largestOddNumber('4206')

solution.largestOddNumber('35427')