class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            result = chr(ord("A") + (n - 1) % 26) + result
            n = (n-1) / 26
        return result
            
            
                


t = Solution()
# print t.convertToTitle(27)
# print t.convertToTitle(5)
print t.convertToTitle(52)
# print t.convertToTitle(30)
# print t.convertToTitle(33)