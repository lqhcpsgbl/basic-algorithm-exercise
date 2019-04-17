class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        check_dict = {}

        for i in magazine:
          if i not in check_dict:
            check_dict[i] = 1
          else:
            check_dict[i] += 1

        for i in ransomNote:
          if i in check_dict:
            check_dict[i] -= 1
            if check_dict[i] < 0:
              return False
          else:
            return False
        return True
