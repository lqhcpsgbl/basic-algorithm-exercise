class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = []
        for i in bin(N)[2:]:
          if i == '1':
            res.append('0')
          else:
            res.append('1')
        return int(''.join(res), 2)
