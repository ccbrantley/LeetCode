class MyStack(object):
  
    def __init__(_self):
        _self.queue = list()

    def push(_self, _x):
        """
        :type x: int
        :rtype: None
        """
        _self.queue.insert(0, _x)

    def pop(_self):
        """
        :rtype: int
        """
        return _self.queue.pop(0)

    def top(_self):
        """
        :rtype: int
        """
        return _self.queue[0]

    def empty(_self):
        """
        :rtype: bool
        """
        return len(_self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
