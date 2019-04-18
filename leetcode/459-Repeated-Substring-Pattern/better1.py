class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        length = len(s)
        for i in range(length / 2 + 1):
          sub_str = s[:i]
          if sub_str and (length % len(sub_str) == 0) and (length / len(sub_str)) * sub_str == s:
            return True
        return False
