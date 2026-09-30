class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        arr=[[] for _ in range(len(nums)+1)]
        for key,val in count.items():
            arr[val].append(key)
        l=len(nums)
        j=0
        while k>0:
            for i in range(len(arr[l-j])):
                ans.append(arr[l-j][i])
                k-=1
            
            j+=1
        return ans

