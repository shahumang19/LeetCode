class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        try:
            if len(s) != len(t): return False
            t = list(t)
            for val in s:
                t.remove(val)
            return True
        except:
            return False
            