class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        chars={}
        for i in s:
            chars[i]=chars.get(i,0)+1
        for i in t:
            if(chars.get(i,0)==0):
                return False
            chars[i]=chars.get(i)-1
        for key,val in chars.items():
            if val>0:
                return False
        return True
        