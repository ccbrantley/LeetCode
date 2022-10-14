class Solution(object):
    def isValid(self, _s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in _s:
            if char == "(":
                stack.append("(")
            elif char == "{":
                stack.append("{")
            elif char == "[":
                stack.append("[")
            elif stack == []:
                return False
            elif char == ")":
                if stack[-1] == "(":
                    del stack[-1]
                else:
                    return False
            elif char == "}":
                if stack[-1] == "{":
                    del stack[-1]
                else:
                    return False
            elif char == "]":
                if stack[-1] == "[":
                    del stack[-1]
                else:
                    return False
        if stack != []:
            return False
        return True
