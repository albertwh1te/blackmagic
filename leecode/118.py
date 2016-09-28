class Solution(object):
    def pascal(self,n):
        if n == 1:
            return [1]
        else:
            upper = self.pascal(n-1)
            return [1] + [upper[i] + upper[i+1] for i in range(n-2)] + [1]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for x in range(1,numRows+1):
            result.append(self.pascal(x))
        return result


test = Solution()
print(test.generate(5))
