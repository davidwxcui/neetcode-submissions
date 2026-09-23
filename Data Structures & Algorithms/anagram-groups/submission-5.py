class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m= defaultdict(list)
        for s in strs:
            key=[0]*26
            for i in s:
                o= ord(i)-ord('a')
                key[o]+=1
            key= tuple(key)
            m[key].append(s)
        return list(m.values())