#190. Reverse Bits    二进制翻转
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        num = bin(n)[2:]    #转化为2进制
        return int(num.zfill(32)[::-1],2)   