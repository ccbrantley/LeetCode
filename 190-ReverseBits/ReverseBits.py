class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int("{:<032}".format("".join([x for x in bin(n)[len(bin(n)):1:-1]])), 2)
