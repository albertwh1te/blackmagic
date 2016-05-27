class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        length = len(digits)
        for i in reversed(xrange(length)):
            digits[i] = digits[i] + 1 + carry if i == length - 1 else digits[
                i] + carry
            carry = 1 if digits[i] == 10 else 0
            if digits[i] == 10:
                    digits[i] = 0
        return [1] + digits if carry == 1 else digits
t = Solution()   
print t.plusOne([9, 9])
