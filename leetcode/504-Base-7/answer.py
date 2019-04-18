class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
          return '0'

        res = []
        less_zero = False
        if num < 0:
          num = -num
          less_zero = True
        while num != 0:
          res.append(str(num % 7))
          num /= 7

        str_res = ''.join(res[::-1])
        if less_zero:
          ret = '-' + str_res
          return ret
        return str_res


if __name__ == '__main__':
  print(Solution().convertToBase7(-7))
