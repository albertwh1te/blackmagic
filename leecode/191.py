class Solution(object):
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0    
        while n > 0:
            i = n % 2
            if i == 1:
                result += 1
            n /= 2
        return result
    def hammingWeight2(self, n):
        return bin(n).count('1')
        

t = Solution()
print t.hammingWeight1(7)    
print t.hammingWeight2(7)    
        