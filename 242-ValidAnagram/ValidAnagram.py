class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictS = {}
        for x in s:
            value = dictS.setdefault(x, 0)
            dictS[x] += 1
        dictT = {}
        for x in t:
            value = dictT.setdefault(x, 0)
            dictT[x] += 1
        for key in dictS.keys():
            value = dictT.setdefault(key, -1)
            if (value == -1):
                return False
            elif (dictS[key] != dictT[key]):
                return False
            else:
                del dictT[key]
        return dictT == {}
