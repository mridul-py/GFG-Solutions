
from typing import List
from collections import Counter

class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        L=[]
        d=Counter(arr)
        for k,v in d.items():
            if(v>=2):
                L.append(k)
        if(L==[]):
            L.append(-1)
        L.sort()
        return L
        
