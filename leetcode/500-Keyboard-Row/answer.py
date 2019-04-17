class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        key_boards = (
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        )
        ret = []
        for word in words:
            for line in key_boards:
                diff = set(word.lower()) - set(line)
                if not diff:
                    ret.append(word)
                    break
        return ret
