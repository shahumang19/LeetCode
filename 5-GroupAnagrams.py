class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_strs = collections.defaultdict(list)
        
        for str_ in strs:
            temp = ''.join(sorted(str_))
            sorted_strs[temp].append(str_)
            
        return sorted_strs.values()           