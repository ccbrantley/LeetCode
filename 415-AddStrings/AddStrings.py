class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        strNumDict = {
            "0" : 0,
            "1" : 1,
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
        }

        numStrList = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]

        nums = (num1, num2) if (len(num1) > len(num2)) else (num2, num1)
        returnString = ""
        carryOver = 0
        for x in range(-1, - len(nums[0]) - 1, -1):
            value = strNumDict[nums[0][x]] + carryOver
            if (len(nums[1]) >= - x):
                value += strNumDict[nums[1][x]] 
            carryOver = value // 10
            remainder = value % 10
            returnString = numStrList[remainder] + returnString
        if (carryOver != 0):
            returnString = numStrList[carryOver] + returnString
        return returnString
