class Solution(object):
    def addStrings(self, num1, num2):

        res, to_add = '', ''
        if len(num1) >= len(num2):
          res, to_add = num1, num2
        else:
          res, to_add = num2, num1
        res = map(int, res[::-1] + '0')
        to_add = map(int, to_add[::-1])
        for index, num in enumerate(to_add):
          res[index] = res[index] + num

        for index, num in enumerate(res):
          if res[index] >= 10:
            res[index + 1] += res[index] / 10
            res[index] %= 10
        
        if res[-1] == 0:
          res.pop()

        return ''.join(map(str, res[::-1]))
