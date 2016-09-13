class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        try:
            for i in ransomNote:
                magazine.remove(i)
            return True
        except:
            return False

t = Solution()
print t.canConstruct("a","b")
print t.canConstruct("aa","aab")

        
