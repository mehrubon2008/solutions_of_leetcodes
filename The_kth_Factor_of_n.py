'''
### Amazon Spring '23 High Frequency ###
#- The kth Factor of n -- Medium -#
#@autor == mehrubon2008 == #
'''

class Solution(object):
    def kthFactor(self=0, n=0, k=0):

        if k == 1:
            return 1
        kol = 0
        for i in range(1, n + 1):
            if n % i == 0:
                kol += 1
            if kol == k:
                return i
        return -1


