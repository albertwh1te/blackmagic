class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        characters = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        while n >= 27:
            result += characters[n % 26-1]
            n /= 26
        if n < 27:
            result = characters[n % 26-1] + result
            return result.upper()
                
                
                


t = Solution()
# print t.convertToTitle(27)
# print t.convertToTitle(5)
print t.convertToTitle(52)
# print t.convertToTitle(30)
# print t.convertToTitle(33)