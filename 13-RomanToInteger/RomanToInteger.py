class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        continueFlag = 0
        for index in range(0, len(s)):
            if continueFlag:
                continueFlag = 0
                continue
            if (s[index] == "I"):
                if (index < len(s) - 1):
                    if (s[index + 1] == "V"):
                        value += 4
                        continueFlag = 1
                    elif (s[index + 1] == "X"):
                        value += 9
                        continueFlag = 1
                    else:
                        value += 1
                else:
                    value += 1
            elif (s[index] == "X"):
                if (index < len(s) - 1):
                    if (s[index + 1] == "L"):
                        value += 40
                        continueFlag = 1
                    elif (s[index + 1] == "C"):
                        value += 90
                        continueFlag = 1
                    else:
                        value += 10
                else:
                    value += 10
            elif (s[index] == "C"):
                if (index < len(s) - 1):
                    if (s[index + 1] == "D"):
                        value += 400
                        continueFlag = 1
                    elif (s[index + 1] == "M"):
                        value += 900
                        continueFlag = 1
                    else:
                        value += 100
                else:
                    value += 100
            elif (s[index] == "V"):
                value += 5
            elif (s[index] == "L"):
                value += 50
            elif (s[index] == "D"):
                value += 500
            elif (s[index] == "M"):
                value += 1000
        return value
