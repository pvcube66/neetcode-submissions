class Solution:
    def clean_string(self,s:str)->str:
        cleaned_s=""
        for i in s:
            if i.isalnum():
                cleaned_s+="".join(i.lower())
        print()
        return cleaned_s
    def isPalindrome(self, s: str) -> bool:
        #approach 1: clean+traverse
        l=0
        
        cleaned_s=self.clean_string(s)
        r=len(cleaned_s)-1
        while(l<=r):
            if(cleaned_s[l]!=cleaned_s[r]):
                return False
            l+=1
            r-=1

        
        return True