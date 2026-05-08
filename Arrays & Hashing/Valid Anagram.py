class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dicts, dictt = {}, {}

        for element1 in range(len(s)):
            dicts[s[element1]] = 1 + dicts.get(s[element1],0)
            dictt[t[element1]] = 1 + dictt.get(t[element1], 0) 

        for value in dicts:
            if dicts[value] != dictt.get(value,0):
                return False
        
        return True
    
s = 'racecar'
t = 'carrace'
print(Solution().isAnagram(s,t))



