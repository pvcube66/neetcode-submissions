class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        currentMax=0
        current=0
        for i in nums:
            seen.add(i)

        for i in range(len(nums)):
            current=1
            if(nums[i]-1 not in seen):
                temp=nums[i]
                while(temp+1 in seen):
                    current+=1
                    temp=temp+1
                currentMax=max(currentMax,current)
                    
            currentMax=max(currentMax,current)
        return max(currentMax,current)


