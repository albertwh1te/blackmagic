class Solution(object):
    def __init__(self):
        self.characters = "abcdefghijklmnopqrstuvwxyz"
        self.s_list = []
        self.t_list = []
    def isAnagram1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.t_list = []
        self.s_list = []
        for i in range(0, len(s)):
            if s[i] in self.characters:
                self.s_list.append(s[i])
    
        for i in range(0, len(t)):
            if t[i] in self.characters:
                self.t_list.append(t[i])
        list_c = [a for a in self.s_list if a not in self.t_list]
        list_b = [a for a in self.s_list if a not in self.t_list]
        if list_c == [] or list_b == []:
            return True
        else:
            return False

    def isAnagram2(self, s, t):
        return sorted(s) == sorted(t)

t = Solution()
print t.isAnagram1(s="anagram", t="iagaram")
print t.isAnagram2(s="anagram", t="nagaram")
print t.isAnagram2(s="ana gram", t="iag aram")

print t.isAnagram1(s="ab", t="a")
