
class Solution:
    def kthElement(self, k, arr1, arr2):
        L=arr1+arr2
        L.sort()
        return L[k-1]
        
        
