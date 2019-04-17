class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        sum_bit = 0
        for i in A:
          # 乘以2
          sum_bit <<= 1
          # 加上最低位
          sum_bit += i
          # 取个位数
          sum_bit %= 5
          if (sum_bit == 0 or sum_bit == 5):
            res.append(True)
          else:
            res.append(False)
        return res
