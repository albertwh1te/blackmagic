class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        i = 0
        while i < len(s):
            old_num = ord(s[i]) - 64
            weight = len(s) - i - 1
            num += old_num * (26 ** weight)
            i += 2
        return num
            
            
            
        
        
t = Solution()
print t.titleToNumber("AA")
print t.titleToNumber("B")
#             
            
