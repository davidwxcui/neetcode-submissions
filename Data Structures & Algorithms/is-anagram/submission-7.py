class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms= defaultdict(int)
        mt = defaultdict(int)

        for i in s:
            ms[i]+=1

        for i in t:
            mt[i]+=1

        return ms == mt