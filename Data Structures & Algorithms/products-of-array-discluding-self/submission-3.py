class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount=0
        productWithoutZeros=1
        for i in range(len(nums)):
            if(nums[i]!=0):
                productWithoutZeros*=nums[i]
            else:
                zeroCount+=1
        
        ans=[0]*len(nums)
        for i in range(len(nums)):
            if(zeroCount>1):
                return ans
            elif(zeroCount==1):
                if(nums[i]==0):
                    ans[i]=productWithoutZeros 

                
            else:
                ans[i]=productWithoutZeros//nums[i]
        return ans
            

        