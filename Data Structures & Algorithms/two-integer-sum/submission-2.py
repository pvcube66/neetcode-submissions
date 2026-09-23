class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        for i in range(len(nums)):
            # if(visited.get(target-nums[i],-1)!=-1):
            if(target-nums[i] in visited):
                return [visited.get(target-nums[i]),i]
            visited[nums[i]]=i
        return []
        
        