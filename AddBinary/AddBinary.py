class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = []
        indexA = len(a) - 1
        indexB = len(b) - 1
        carry = 0
        while indexA >= 0 or indexB >= 0:
            while indexA >= 0 and indexB >= 0:
                valueA = a[indexA]
                valueB = b[indexB]
                if (valueA == "1" and valueB == "1" ):
                    if (carry):
                        c.insert(0, "1")
                    else:
                        c.insert(0, "0")
                    carry = 1
                elif (valueA == "1"  or valueB == "1" ):
                    if (carry):
                        c.insert(0, "0")
                        carry = 1
                    else:
                        c.insert(0, "1")
                else:
                    if (carry):
                        c.insert(0, "1")
                        carry = 0
                    else:
                        c.insert(0, "0")  
                indexA -= 1
                indexB -= 1
            while indexA >= 0:
                valueA = a[indexA]
                if (valueA == "1" ):
                    if (carry):
                        c.insert(0, "0")
                        carry = 1
                    else:
                        c.insert(0, "1")
                else:
                    if (carry):
                        c.insert(0, "1")
                        carry = 0
                    else:
                        c.insert(0, "0")
                indexA -= 1
            while indexB >= 0:
                valueB = b[indexB]
                if (valueB == "1" ):
                    if (carry):
                        c.insert(0, "0")
                        carry = 1
                    else:
                        c.insert(0, "1")
                else:
                    if (carry):
                        c.insert(0, "1")
                        carry = 0
                    else:
                        c.insert(0, "0")
                indexB -= 1
            if (carry):
                c.insert(0, "1")
                carry = 0
        return ''.join(c)
