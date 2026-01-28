class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs: 
            return ""

        
        prefix = strs[0]

        for i in range(len(prefix)):
            for j in strs[1:]:
                if i >= len(j) or j[i] != prefix[i]:
                    return prefix[:i]

        return prefix

