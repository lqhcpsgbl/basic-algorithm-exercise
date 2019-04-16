class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stack_a = []
        stack_b = []
        for i in S:
          if i == '#':
            if stack_a:
              stack_a.pop()
          else:
            stack_a.append(i)

        for j in T:
          if j == '#':
            if stack_b:
              stack_b.pop()
          else:
            stack_b.append(j)
        return ''.join(stack_a) == ''.join(stack_b)

if __name__ == '__main__':
  Solution().backspaceCompare('ab#c', 'ad#c')