class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current=1
        max_count=1
        nums.sort()
        i=1
        while(i<len(nums)):
            if(nums[i-1]==nums[i]):
                i+=1
                continue
            if(nums[i-1]+1==nums[i]):
                current+=1
            else:
                max_count=max(current,max_count)
                current=1

            i+=1
        return max(max_count,current)