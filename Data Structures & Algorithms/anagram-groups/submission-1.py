class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        # result=[]
        for i in range(len(strs)):
            ele="".join(sorted(strs[i]))
            if ele in groups:
                groups[ele].append(strs[i])
            else:
                groups[ele]=[strs[i]]
        # for k,v in groups.items():
        #     result.append(v)
        return list(groups.values())

        
        