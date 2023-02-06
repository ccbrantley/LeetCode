class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for index in range(1, n + 1):
            div3 = index % 3 == 0
            div5 = index % 5 == 0
            if (div3 and div5):
                answer.append("FizzBuzz")
            elif (div3):
                answer.append("Fizz")
            elif (div5):
                answer.append("Buzz")
            else:
                answer.append(str(index))
        return answer
