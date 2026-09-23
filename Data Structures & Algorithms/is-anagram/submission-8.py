class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x= defaultdict(int)
        y= defaultdict(int)
        for i in s:
            if i in x:
                x[i]+=1
            else:
                x[i]=1
        for j in t:
            if j in y:
                y[j]+=1
            else:
                y[j]=1
        return x==y