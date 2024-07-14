'''
### Amazon Spring '23 High Frequency ###
#- Optimal Partition of String -- Medium -#
#@autor == mehrubon2008 == #
'''


class Solution(object):
    def partitionString(self=0, s=0):
        kol = 1
        substring = ""
        for i in s:
            if i not in substring:
                substring += i
            else:
                kol += 1
                substring = i
        return kol
print(Solution.partitionString(s = 'ssssss'))
