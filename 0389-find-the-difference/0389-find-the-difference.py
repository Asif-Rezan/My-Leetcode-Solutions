class Solution(object):
    def findTheDifference(self, s, t):
        
        s,t = Counter(s), Counter(t)

        for c in t:
            if c not in s:
                return c
            if s[c] < t[c]:
                return c

        


        