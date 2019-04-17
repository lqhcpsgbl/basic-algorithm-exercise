# https://leetcode.com/problems/count-and-say/

def get_num(start):

    index = 0
    count = 1
    length = len(start)

    temp_list = []

    while True:
        next_one = index + 1
        if next_one >= length:
            temp = str(count) + start[index]
            break
        else:
            if start[index] == start[next_one]:
                count += 1
            else:
                temp = str(count) + start[index]
                temp_list.append(temp)
                count = 1

        index += 1
    
    temp_list.append(temp)
    return ''.join(temp_list)


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        start = '1'
        for i in range(1, n):
            start = get_num(start)
        return start
