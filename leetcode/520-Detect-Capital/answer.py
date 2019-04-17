class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if all((i.islower() for i in word)) or all((i.isupper() for i in word)):
          return True
        if word[0].isupper() and all((i.islower() for i in word[1:])):
          return True
        return False
