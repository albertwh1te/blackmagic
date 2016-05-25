class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "AEIOUaeiou"
        characters = []
        result = []
        for character in s:
            if character in vowels:
                characters.append(character)
        for character in s:
            if character in vowels:
                character = characters.pop()
                result.append(character)
            else:
                result.append(character)
        return "".join(result)
        
t=Solution()
print t.reverseVowels("hello")