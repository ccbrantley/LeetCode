class MyQueue(object):

    def __init__(_self):
        _self.queue = []

    def push(_self, _x):
        """
        :type x: int
        :rtype: None
        """
        _self.queue.append(_x)

    def pop(_self):
        """
        :rtype: int
        """
        return _self.queue.pop(0)

    def peek(_self):
        """
        :rtype: int
        """
        return _self.queue[0]

    def empty(_self):
        """
        :rtype: bool
        """
        return len(_self.queue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
