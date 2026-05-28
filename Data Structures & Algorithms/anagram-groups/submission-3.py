class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for s in strs:
            alp=[0]*26
            for i in s:
               idx=ord(i)-ord('a')
               alp[idx]+=1
            res[tuple(alp)].append(s)

        return list(res.values())