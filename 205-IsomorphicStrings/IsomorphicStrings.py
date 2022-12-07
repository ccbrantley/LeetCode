class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping1 = {}
        mapping2 = {}
        for x in range(len(s)):
            value = mapping1.setdefault(s[x], t[x])
            if (value != t[x]):
                return False
            value = mapping2.setdefault(t[x], s[x])
            if (value != s[x]):
                return False
        return True
