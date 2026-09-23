class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x= defaultdict(int)
        y= defaultdict(int)
        for i in s:
            x[i]+=1

        for j in t:
            y[j]+=1

        return x==y